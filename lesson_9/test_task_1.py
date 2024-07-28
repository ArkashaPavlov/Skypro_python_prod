from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text
import pytest
import requests

#=========api vars============
base_url = "https://x-clients-be.onrender.com"

@pytest.fixture
def auth_token():
    response = requests.post(f"{base_url}/auth/login", json={"username": "raphael", "password": "cool-but-crude"})
    return response.json()["userToken"]

@pytest.fixture
def company_id(auth_token):
    headers = {
        "x-client-token": auth_token,
        "Content-Type": "application/json"
    }
    new_company = {
        "name": "Aboba and Lupa",
        "description": "do the great memes"
    }
    response = requests.post(f"{base_url}/company", json=new_company, headers=headers)
    return response.json()["id"]

#=========db vars=============
db_connection_string = "postgresql://x_clients_db_3fmx_user:mzoTw2Vp4Ox4NQH0XKN3KumdyAYE31uq@dpg-cour99g21fec73bsgvug-a.oregon-postgres.render.com/x_clients_db_3fmx"
#=============================


def test_get_employees(auth_token, company_id):
    headers = {"x-client-token": auth_token}
    response = requests.get(f"{base_url}/employee", params={"company": company_id}, headers=headers)

    db = create_engine(db_connection_string)
    params ={
        "company_id": company_id
    }

    emps_in_com = db.execute(text("select * from employee where company_id = :company_id"), params).fetchall()
    
    assert len(response.json()) == len(emps_in_com) # 0 == 0
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_employee_by_id(auth_token, company_id):
    headers = {"x-client-token": auth_token}

    new_employee = {
        "firstName": "Viktor",
        "lastName": "Korneplod",
        "companyId": company_id,
        "email": "Korneplod@dot.com",
        "phone": "1234567890",
        "isActive": True
    }
    response = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)
    employee_id = response.json()["id"]
    
    response = requests.get(f"{base_url}/employee/{employee_id}", headers=headers)
    
    
    db = create_engine(db_connection_string)
    params ={
        "emp_id": employee_id
    }

    emp_by_id = db.execute(text("select * from employee where id = :emp_id"), params).fetchall()

    assert response.status_code == 200

    assert employee_id == emp_by_id[0][0]
    assert response.json()["firstName"] == emp_by_id[0][4]

def test_create_employee(auth_token, company_id):
    
    db = create_engine(db_connection_string)
    count_emps_before = len(db.execute("select * from employee").fetchall())
    
    headers = {
        "x-client-token": auth_token,
        "Content-Type": "application/json"
    }
    new_employee = {
        "firstName": "Viktor_new",
        "lastName": "Korneplod_v2",
        "companyId": company_id,
        "email": "Korneplod@example.com",
        "phone": "1234567890",
        "isActive": True
    }
    response = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)

    params ={
        "emp_id": response.json()["id"]
    }

    count_emps_after = len(db.execute("select * from employee").fetchall())
    emp_by_id = db.execute(text("select * from employee where id = :emp_id"), params).fetchall()

    assert response.status_code == 201

    assert count_emps_before < count_emps_after
    assert count_emps_before == count_emps_after - 1
    assert emp_by_id[0][0] == response.json()["id"]

def test_update_employee(auth_token, company_id):
    
    db = create_engine(db_connection_string)
    headers = {
        "x-client-token": auth_token,
        "Content-Type": "application/json"
    }

    new_employee = {
        "firstName": "Viktor",
        "lastName": "Korneplod",
        "companyId": company_id,
        "email": "Korneplod@dot.com",
        "phone": "1234567890",
        "isActive": True
    }

    response = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)
    employee_id = response.json()["id"]
    
    params_to_db = {
        "com_id":company_id
    }

    count_emps_before = len(db.execute(text("select * from employee where company_id = :com_id"), params_to_db).fetchall())

    updated_data = {
        "firstName": "Changed_Vitaliy",
        "email": "pomenyal@yandex.com"
    }

    response = requests.patch(f"{base_url}/employee/{employee_id}", json=updated_data, headers=headers)
    

    count_emps_after = len(db.execute(text("select * from employee where company_id  = :com_id"),params_to_db).fetchall())

    assert count_emps_before == count_emps_after

    assert response.status_code == 200
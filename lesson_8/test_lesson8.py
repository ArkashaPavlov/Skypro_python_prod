import pytest
import requests

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
        "name": "Test Company",
        "description": "A company for testing purposes"
    }
    response = requests.post(f"{base_url}/company", json=new_company, headers=headers)
    return response.json()["id"]

def test_get_employees(auth_token, company_id):
    headers = {"x-client-token": auth_token}
    response = requests.get(f"{base_url}/employee", params={"company": company_id}, headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_employee_by_id(auth_token, company_id):
    headers = {"x-client-token": auth_token}

    new_employee = {
        "firstName": "John",
        "lastName": "Doe",
        "companyId": company_id,
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "isActive": True
    }
    response = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)
    employee_id = response.json()["id"]
    
    response = requests.get(f"{base_url}/employee/{employee_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == employee_id

def test_create_employee(auth_token, company_id):
    headers = {
        "x-client-token": auth_token,
        "Content-Type": "application/json"
    }
    new_employee = {
        "firstName": "John",
        "lastName": "Doe",
        "companyId": company_id,
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "isActive": True
    }
    response = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)
    assert response.status_code == 201

def test_update_employee(auth_token, company_id):
    headers = {
        "x-client-token": auth_token,
        "Content-Type": "application/json"
    }

    new_employee = {
        "firstName": "John",
        "lastName": "Doe",
        "companyId": company_id,
        "email": "john.doe@example.com",
        "phone": "1234567890",
        "isActive": True
    }
    response = requests.post(f"{base_url}/employee", json=new_employee, headers=headers)
    employee_id = response.json()["id"]
    

    updated_data = {
        "lastName": "Smith",
        "email": "john.smith@example.com"
    }
    response = requests.patch(f"{base_url}/employee/{employee_id}", json=updated_data, headers=headers)
    assert response.status_code == 200

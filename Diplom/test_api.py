import pytest
import requests
import random
import string

base_url = "https://lk.alltel24.ru/"
login = 'oleg@alltel24.ru'
password = '9xN$5qV*7qS&3sQ%'

def random_char(char_num):
       return ''.join(random.choice(string.ascii_letters) for _ in range(char_num))

def random_digits(char_num):
    first_digit = random.choice(string.digits[1:])
    other_digits = ''.join(random.choice(string.digits) for _ in range(char_num - 1))
    return first_digit + other_digits


@pytest.mark.parametrize('login, password',[(login, password)])
def test_get_auth_token(login, password):
    my_json = {
        "email": login,
         "password": password

    }

    response = requests.get(f"{base_url}api/auth/v1/auth/token-generate", json= my_json)
    resp_body = response.json()
    token = resp_body.get("data", {}).get("access_token")

    assert response.status_code == 200
    assert token != ""
    return token

@pytest.mark.parametrize('limit',[(10),(2),(4),(7)])
def test_get_users_list(limit):
    my_headers = {
        "Authorization": f"Bearer {test_get_auth_token(login, password)}",
        "Content-Type": "application/json"
        }

    my_params = {
        "limit": limit
        }
    response = requests.get(f"{base_url}api/company/v1/employee/list", params= my_params, headers= my_headers)
    resp_body = response.json()

    
    assert response.status_code == 200

@pytest.mark.parametrize('login, password',[(login, password)])
def test_create_user(login, password):
    my_headers = {
        "Authorization": f"Bearer {test_get_auth_token(login, password)}",
        "Content-Type": "application/json"
        }

    my_json = {
        "name": f"{random_char(4)}_API",
        "email": f"{random_char(2)}@skypro.ru",
        "phone": None,
        "password": f"12#{random_char(4)}!&",
        "role": "user",
        "is_active": True
    }


    response = requests.post(f"{base_url}api/company/v1/employee/create",headers=my_headers ,json= my_json)
    resp_body = response.json()

    user_id = resp_body.get("data", {}).get("id")
    assert response.status_code == 200
    return user_id

@pytest.mark.parametrize('login, password',[(login, password)])
def test_create_internal(login, password):
    my_headers = {
        "Authorization": f"Bearer {test_get_auth_token(login, password)}",
        "Content-Type": "application/json"
        }
    
    my_json = {
    "employee": {
        "id": test_create_user(login, password),
        "name": ""
        },
    "forward": {
        "enabled": False,
        "target": {
            "type": "internal",
            "condition": "direct",
            "delay": 20,
            "data": "101",
            "notification": {
                "enabled": False,
                "driver": {
                    "name": "email",
                    "data": "apiMail@skypro.ru"
                }
            }
        }
    },
    "ip": "0.0.0.0",
    "is_active": True,
    "line": {
        "provider":"mtt",
        "phone": "73432281488"
    },
    "password": f"{random_char(5)}23&%",
    "short_number": random_digits(3)
    }
     
    response = requests.post(f"{base_url}api/company/v1/internal-number/add",headers=my_headers ,json= my_json)
    print(response.json())
    assert response.status_code == 200
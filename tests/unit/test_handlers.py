from flask import jsonify, request
from unittest.mock import patch
import json


from employee import config
from employee import handlers
from employee.logic import emp_info

def test_get_emp(mocker, client):
    mocker.patch.object(
        emp_info, 'get_emp', return_value = {
    "birth_day": [
        "Thu, 21 Dec 1995 00:00:00 GMT"
    ],
    "date_hired": [
        "Thu, 05 Sep 2019 00:00:00 GMT"
    ],
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "gender": [
        "M"
    ],
    "last_name": [
        "Dalvi"
    ],
    "updated": [
        "Sat, 20 Nov 2021 19:06:58 GMT"
    ]
})

    handler_response = client.get('/employee/2')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "birth_day": [
        "Thu, 21 Dec 1995 00:00:00 GMT"
    ],
    "date_hired": [
        "Thu, 05 Sep 2019 00:00:00 GMT"
    ],
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "gender": [
        "M"
    ],
    "last_name": [
        "Dalvi"
    ],
    "updated": [
        "Sat, 20 Nov 2021 19:06:58 GMT"
    ]
}


def test_get_emp_salary(mocker, client):
    mocker.patch.object(
        emp_info, 'get_emp_salary', return_value = {
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "salary": [
        300000
    ]
})

    handler_response = client.get('/salary/2')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "salary": [
        300000
    ]
}
        

def test_get_emp_by_manager(mocker, client):
    mocker.patch.object(
        emp_info, 'get_emp_by_manager', return_value = {
    "dept_id": [
        "IT"
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "manager_id": [
        1
    ]
})

    handler_response = client.get('/manager/1')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "dept_id": [
        "IT"
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "manager_id": [
        1
    ]
}



def test_get_emp_dept(mocker, client):
    mocker.patch.object(
        emp_info, 'get_emp_dept', return_value = {
    "dept_id": [
        "IT"
    ],
    "dept_name": [
        "IT Services"
    ],
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ]
})

    handler_response = client.get('/department/IT Services')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "dept_id": [
        "IT"
    ],
    "dept_name": [
        "IT Services"
    ],
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ]
}


def test_get_salary_range(mocker, client):
    mocker.patch.object(
        emp_info, 'get_salary_range', return_value = {
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "salary": [
        300000
    ]
})

    handler_response = client.get('/salary/250000-300000')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "salary": [
        300000
    ]
}


def test_get_manager_dept(mocker, client):
    mocker.patch.object(
        emp_info, 'get_manager_dept', return_value = {
    "dept_id": [
        "IT"
    ],
    "dept_name": [
        "IT Services"
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "manager_id": [
        1
    ]
})

    handler_response = client.get('/department/1/IT')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "dept_id": [
        "IT"
    ],
    "dept_name": [
        "IT Services"
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "manager_id": [
        1
    ]
}


def test_get_leaves_employee(mocker, client):
    mocker.patch.object(
        emp_info, 'get_leaves_employee', return_value = {
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "leaves_left": [
        0
    ],
    "leaves_taken": [
        21
    ],
    "unpaid_leaves": [
        7
    ]
})

    handler_response = client.get('/leaves/2')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
    "emp_id": [
        2
    ],
    "first_name": [
        "Shwetang"
    ],
    "last_name": [
        "Dalvi"
    ],
    "leaves_left": [
        0
    ],
    "leaves_taken": [
        21
    ],
    "unpaid_leaves": [
        7
    ]
}





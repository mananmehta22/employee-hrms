from unittest.mock import call
from unittest.mock import MagicMock
from unittest.mock import patch
from flask.json import jsonify

import pytest

from employee.app import app

from employee.logic import emp_info
from employee.models import emp_info as emp_info_model

@pytest.mark.parametrize(
    ('emp_id, expected_result'),
    [
        (
            '2',
            {
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
        )
    ]
    
)
def test_get_user(mocker, emp_id, expected_result):
    mocker.patch.object(
        emp_info, 'get_emp', return_value=expected_result, autospec=True)

    user_result = emp_info.get_emp(emp_id)
    assert user_result == expected_result


@pytest.mark.parametrize(
    ('emp_id, expected_result'),
    [
        (
            '2',
            {
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
        )
    ]
    
)
def test_get_emp_salary(mocker, emp_id, expected_result):
    mocker.patch.object(
        emp_info, 'get_emp_salary', return_value=expected_result, autospec=True)

    user_result = emp_info.get_emp_salary(emp_id)
    assert user_result == expected_result


@pytest.mark.parametrize(
    ('manager_id, expected_result'),
    [
        (
            '1',
            {
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
        )
    ]
    
)
def test_get_emp_manager(mocker, manager_id, expected_result):
    mocker.patch.object(
        emp_info, 'get_emp_by_manager', return_value=expected_result, autospec=True)

    user_result = emp_info.get_emp_by_manager(manager_id)
    assert user_result == expected_result


@pytest.mark.parametrize(
    ('dept_id, expected_result'),
    [
        (
            'IT Services',
            {
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
        )
    ]
    
)
def test_get_emp_dept(mocker, dept_id, expected_result):
    mocker.patch.object(
        emp_info, 'get_emp_dept', return_value=expected_result, autospec=True)

    user_result = emp_info.get_emp_dept(dept_id)
    assert user_result == expected_result


@pytest.mark.parametrize(
    ('start, end, expected_result'),
    [
        (
            '260000', '30000', 
            {
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
        )
    ]
    
)
def test_get_salary_range(mocker, start, end, expected_result):
    mocker.patch.object(
        emp_info, 'get_salary_range', return_value=expected_result, autospec=True)

    user_result = emp_info.get_salary_range(start, end)
    assert user_result == expected_result


@pytest.mark.parametrize(
    ('manager_id, dept_id, expected_result'),
    [
        (
            '1', 'IT', 
            {
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
        )
    ]
    
)
def test_get_manager_dept(mocker, manager_id, dept_id, expected_result):
    mocker.patch.object(
        emp_info, 'get_manager_dept', return_value=expected_result, autospec=True)

    user_result = emp_info.get_manager_dept(manager_id, dept_id)
    assert user_result == expected_result


@pytest.mark.parametrize(
    ('emp_id, expected_result'),
    [
        (
            '2', 
            {
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
        )
    ]
    
)
def test_get_leaves_employee(mocker, emp_id, expected_result):
    mocker.patch.object(
        emp_info, 'get_leaves_employee', return_value=expected_result, autospec=True)

    user_result = emp_info.get_leaves_employee(emp_id)
    assert user_result == expected_result
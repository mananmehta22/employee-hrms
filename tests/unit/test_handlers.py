"""Test Module of Handlers."""
import json

from employee.logic import emp_info


def test_get_emp(mocker, client):
    """Test Get Employee Information."""
    mocker.patch.object(
        emp_info,
        'get_emp',
        return_value={
            'birth_day': ['Thu, 21 Dec 1995 00:00:00 GMT'],
            'date_hired': ['Thu, 05 Sep 2019 00:00:00 GMT'],
            'emp_id': [2],
            'first_name': ['Shwetang'],
            'gender': ['M'],
            'last_name': ['Dalvi'],
            'updated': ['Sat, 20 Nov 2021 19:06:58 GMT'],
        },
    )

    handler_response = client.get('/employee/2')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
        'birth_day': ['Thu, 21 Dec 1995 00:00:00 GMT'],
        'date_hired': ['Thu, 05 Sep 2019 00:00:00 GMT'],
        'emp_id': [2],
        'first_name': ['Shwetang'],
        'gender': ['M'],
        'last_name': ['Dalvi'],
        'updated': ['Sat, 20 Nov 2021 19:06:58 GMT'],
    }


def test_get_emp_salary(mocker, client):
    """Test Get Employee Salary."""
    mocker.patch.object(
        emp_info,
        'get_emp_salary',
        return_value={
            'emp_id': [2],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
            'salary': [300000],
        },
    )

    handler_response = client.get('/salary/2')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
        'emp_id': [2],
        'first_name': ['Shwetang'],
        'last_name': ['Dalvi'],
        'salary': [300000],
    }


def test_get_emp_by_manager(mocker, client):
    """Test Get Employees under a manager."""
    mocker.patch.object(
        emp_info,
        'get_emp_by_manager',
        return_value={
            'dept_id': ['IT'],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
            'manager_id': [1],
        },
    )

    handler_response = client.get('/manager/1')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
            'dept_id': ['IT'],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
            'manager_id': [1],
    }


def test_get_emp_dept(mocker, client):
    """Test Get Employees under Single Department."""
    mocker.patch.object(
        emp_info,
        'get_emp_dept',
        return_value={
            'dept_id': ['IT'],
            'dept_name': ['IT Services'],
            'emp_id': [2],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
        },
    )

    handler_response = client.get('/department/IT Services')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
        'dept_id': ['IT'],
        'dept_name': ['IT Services'],
        'emp_id': [2],
        'first_name': ['Shwetang'],
        'last_name': ['Dalvi'],
    }


def test_get_salary_range(mocker, client):
    """Test Get Employees under salary range."""
    mocker.patch.object(
        emp_info,
        'get_salary_range',
        return_value={
            'emp_id': [2],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
            'salary': [300000],
        },
    )

    handler_response = client.get('/salary/250000-300000')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
        'emp_id': [2],
        'first_name': ['Shwetang'],
        'last_name': ['Dalvi'],
        'salary': [300000],
    }


def test_get_manager_dept(mocker, client):
    """Test Get Manager of a department."""
    mocker.patch.object(
        emp_info,
        'get_manager_dept',
        return_value={
            'dept_id': ['IT'],
            'dept_name': ['IT Services'],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
            'manager_id': [1],
        },
    )

    handler_response = client.get('/department/1/IT')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
        'dept_id': ['IT'],
        'dept_name': ['IT Services'],
        'first_name': ['Shwetang'],
        'last_name': ['Dalvi'],
        'manager_id': [1],
    }


def test_get_leaves_employee(mocker, client):
    """Test Get Leaves of the employee."""
    mocker.patch.object(
        emp_info,
        'get_leaves_employee',
        return_value={
            'emp_id': [2],
            'first_name': ['Shwetang'],
            'last_name': ['Dalvi'],
            'leaves_left': [0],
            'leaves_taken': [21],
            'unpaid_leaves': [7],
        },
    )

    handler_response = client.get('/leaves/2')
    assert handler_response.status_code == 200
    result = json.loads(handler_response.data.decode())
    assert result == {
        'emp_id': [2],
        'first_name': ['Shwetang'],
        'last_name': ['Dalvi'],
        'leaves_left': [0],
        'leaves_taken': [21],
        'unpaid_leaves': [7],
    }


def test_apply_for_leaves(mocker, client):
    """Test Get Unpaid Leaves."""
    mocker.patch.object(
        emp_info,
        'apply_for_leaves',
        return_value='Your leave application was successful!',
    )

    handler_response = client.put('/apply/3/3', follow_redirects=True)
    encoding = 'utf-8'
    temp = handler_response.data  # noqa: F841
    temp1 = handler_response.response[0]
    result = str(temp1, encoding)
    assert handler_response.status_code == 200
    assert result == 'Your leave application was successful!'


def test_set_employee(mocker, client):
    """Update Employee."""
    mocker.patch.object(
        emp_info, 'set_employee', return_value='Employee Data \
                                                Succesfully updated!'
    )

    handler_response = client.put(
        '/update/employee?emp_no=1&first_name=Shreyaa&last_name=Mendhe \
        &birth_date=1994-04-05&gender=F&hire_date=2015-03-07 \
        &salary=300000&dept_no=RA',
        follow_redirects=True,
    )
    encoding = 'utf-8'
    temp = handler_response.data  # noqa: F841
    temp1 = handler_response.response[0]
    result = str(temp1, encoding)
    assert handler_response.status_code == 200
    assert result == 'Employee Data Succesfully updated!'

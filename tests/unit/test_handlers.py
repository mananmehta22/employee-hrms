from flask import jsonify, request
from unittest.mock import patch


from employee import config
from employee import handlers
from employee.logic import emp_info

def test_get_emp(mocker, client):
    mocker.patch.object(
        emp_info, 'get_emp', return_value = jsonify([2, "Shwetang", "Dalvi", "Thu, 21 Dec 1995 00:00:00 GMT", "M", "Thu, 05 Sep 2019 00:00:00 GMT", "Sat, 20 Nov 2021 19:06:58 GMT"]))

    handler_response = client.get('/employee/2')
    assert handler_response.status_code == 200
    result = jsonify.loads(handler_response.data.decode())
    assert result == [2, "Shwetang", "Dalvi", "Thu, 21 Dec 1995 00:00:00 GMT", "M", "Thu, 05 Sep 2019 00:00:00 GMT", "Sat, 20 Nov 2021 19:06:58 GMT"]


def test_get_salary(mocker, client):
    mocker.patch.object(
        emp_info, 'get_salary', return_value = jsonify([2, "Shwetang", "Dalvi", 300000]))

    handler_response = client.get('/salary/2')
    assert handler_response.status_code == 200
    result = jsonify.loads(handler_response.data.decode())
    assert result == [2, "Shwetang", "Dalvi", 300000]
        
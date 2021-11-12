"""Handlers.

All the different endpoints are used to identify a user based on a
login and a password.
"""

from employee.app import app
from employee.logic import emp_info


@app.route('/hello')
def hello_world():
    return 'Hello World', 200

@app.route('/employee/<id>', methods='GET')
def get_employee():
    return flaskify(emp_info.get_employee())


@app.route('/employee/<id>/salary', methods = 'GET')
def get_salary():
    return flaskify()

@app.route('/employee/<department>', methods = 'GET')
def single_department():
    return flaskify()

@app.route('/employee/<manager>', methods = 'GET')
def get_manager():
    return flaskify()


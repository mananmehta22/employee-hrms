"""Handlers.

All the different endpoints are used to identify a user based on a
login and a password.
"""

import flask
from employee.app import app
from employee.logic import emp_info
from flask import Flask


@app.route('/hello')
def hello_world():
    return 'Hello World', 200

@app.route('/employee/<id>', methods='GET')
def get_employee():
    return flask(emp_info.get_emp())


@app.route('/employee/<id>/salary', methods = 'GET')
def get_salary():
    return flask(emp_info.get_emp_salary())


@app.route('/employee/<department>', methods = 'GET')
def single_department():
    return flask(emp_info.get_emp_dept())


@app.route('/employee/<manager>', methods = 'GET')
def get_manager():
    return flask(emp_info.get_emp_by_manager())

@app.route('/employee/salary/range', methods = 'GET')
def get_salary_range():
    return flask(emp_info.get_salary_range)

@app.route('/employee/manager/<department>', methods = 'GET')
def get_manager_dept():
    return flask(emp_info.get_manager_dept)

@app.route('/employee/leaves', methods = 'GET')
def get_leaves_employee():
    return flask(emp_info.get_leaves_employee)

@app.route('/employee/leaves_without_pay', methods = 'GET')
def get_leaves_without_pay():
    return flask(emp_info.get_leaves_without_pay)

@app.route('/employee/leaves_without_pay', methods = 'GET')
def get_leaves_taken():
    return flask(emp_info.get_leaves_without_pay)

@app.route('/employee/add-employee', methods = ['PUT', 'GET'])
def add_employee():
    return flask(emp_info.set_employee)




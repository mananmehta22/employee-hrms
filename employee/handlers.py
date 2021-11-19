"""Handlers.

All the different endpoints are used to identify a user based on a
login and a password.
"""

import flask
from employee.app import app
from employee.logic import emp_info
from flask import Flask
from flask.json import jsonify


@app.route('/')
def hello_world():
    return 'Hello World', 200

@app.route('/employee/<int:emp_no>/', methods=['GET'])
def get_emp(emp_no):
    return emp_info.get_emp(emp_no)


@app.route('/employee/<int:emp_no>/<int:salary>/', methods = ['GET'])
def get_salary(emp_no, salary):
    return emp_info.get_emp_salary(emp_no, salary)


@app.route('/department/<manager>/', methods = ['GET'])
def get_manager():
    return emp_info.get_manager_dept()

@app.route('/employee/<department>/', methods = ['GET'])
def single_department():
    return emp_info.get_emp_dept()

@app.route('/employee/salary/range/', methods = ['GET'])
def get_salary_range():
    return emp_info.get_salary_range

@app.route('/employee/manager/<department>/', methods = ['GET'])
def get_manager_dept():
    return emp_info.get_manager_dept

@app.route('/employee/leaves/', methods = ['GET'])
def get_leaves_employee():
    return emp_info.get_leaves_employee

@app.route('/employee/leaves_without_pay/', methods = ['GET'])
def get_leaves_without_pay():
    return emp_info.get_leaves_without_pay

@app.route('/employee/leaves_without_pay/', methods = ['GET'])
def get_leaves_taken():
    return emp_info.get_leaves_without_pay

@app.route('/employee/add-employee/', methods = ['PUT', 'GET'])
def add_employee():
    return emp_info.set_employee




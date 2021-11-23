import re
import flask
from werkzeug.wrappers import request, response
from employee.app import app
from employee.logic import emp_info
from flask import Flask, redirect



@app.route('/')
def hello_world():
    return 'Hello World', 200

@app.route('/employee/<int:emp_no>', methods=['GET'])
def get_emp(emp_no):
    return emp_info.get_emp(emp_no)


@app.route('/salary/<int:emp_no>', methods = ['GET'])
def get_salary(emp_no):
    return emp_info.get_emp_salary(emp_no)


@app.route('/manager/<int:manager_id>', methods = ['GET'])
def get_emp_manager(manager_id):
    return emp_info.get_emp_by_manager(manager_id)

@app.route('/department/<string:dept_name>', methods = ['GET'])
def single_department(dept_name):
    return emp_info.get_emp_dept(dept_name)

@app.route('/salary/<int:start>-<int:end>', methods = ['GET'])
def get_salary_range(start,end):
    return emp_info.get_salary_range(start,end)

@app.route('/department/<int:manager_id>/<string:dept_no>', methods = ['GET'])
def get_manager_dept(manager_id,dept_no):
    return emp_info.get_manager_dept(manager_id, dept_no)

@app.route('/employee/leaves', methods = ['GET'])
def get_leaves_employee():
    return emp_info.get_leaves_employee

@app.route('/employee/leaves_without_pay', methods = ['GET'])
def get_leaves_without_pay():
    return emp_info.leaves_without_pay()


@app.route('/apply/<int:emp_no>/<int:applied_leaves>', methods = ['PUT', 'GET'])
def apply_for_leaves(emp_no, applied_leaves):
    emp_info.apply_for_leaves(emp_no, applied_leaves)
    return redirect ('/successful')

@app.route('/successful')
def redirected():
    return "Your leave application was successful!"


@app.route('/add-employee', methods = ['PUT'])
def set_employee():
    emp_no = flask.request.args['emp_no']
    first_name = flask.request.args['first_name']
    last_name = flask.request.args['last_name']
    birth_date = flask.request.args['birth_date']
    gender = flask.request.args['gender']
    hire_date = flask.request.args['hire_date']
    salary = flask.request.args['salary']
    dept_no = flask.request.args['dept_no']
    emp_info.set_employee(emp_no, first_name, last_name, birth_date, gender, hire_date, salary, dept_no)
    return redirect ('/update')

@app.route('/update')
def update():
    return "Employee Data Succesfully updated!"


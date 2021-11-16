from datetime import datetime
from time import time

from flask import current_app, g, request, response
from flask.globals import request
from flask_executor import Executor


from employee.models import emp_info

def get_emp(emp_id):
    result = emp_info.get_emp(emp_id)

    
    if emp_id != type(int):
        return response.create_error_response(
            status=400, message='Invalid input.')

    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')
    return result



def get_emp_salary(emp_id, emp_salary):
    result = emp_info.get_emp_salary(emp_id, emp_salary)

    if emp_id and emp_salary != type(int):
         return response.create_error_response(
            status=400, message='Invalid input.')

    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')
    return result


def get_emp_by_manager(manager_id):
    result = emp_info.get_emp_by_manager(manager_id)

    if manager_id != type(int):
         return response.create_error_response(
            status=400, message='Invalid input.')

    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')
    return result



def get_emp_dept():
    result = emp_info.get_emp_dept()
    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')
    return result


def get_salary_range(start, end):
    result = emp_info.get_salary_range(start, end)

    if start and end != type(int):
         return response.create_error_response(
            status=400, message='Invalid input.')

    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')

    return result

def get_manager_dept(manager_id, dept_no):
    result = emp_info.get_emp_by_manager(manager_id, dept_no)

    if manager_id and dept_no != type(int):
         return response.create_error_response(
            status=400, message='Invalid input.')

    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')
    return result

def get_leaves_employee(emp_no):
    result = emp_info.get_leaves_employee(emp_no)

    if emp_no != type(int):
         return response.create_error_response(
            status=400, message='Invalid input.')

    if not result:
         return response.create_error_response(
            status=400,
            message='No such record present')
    return result

        

    

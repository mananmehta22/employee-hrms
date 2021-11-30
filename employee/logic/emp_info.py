from datetime import date, datetime
from pdb import set_trace
from time import time

from flask import current_app, g, json, request, jsonify
from flask.globals import request
from sqlalchemy.sql.sqltypes import CHAR


from employee.models import emp_info
from employee.connectors import mysql


def get_emp(emp_no):
    if type(emp_no) != int:
        return jsonify(
            status=400, message='Invalid input.')

    result = emp_info.get_emp(emp_no)

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result



def get_emp_salary(emp_no):
    result = emp_info.get_emp_salary(emp_no)

    if type(emp_no) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result


def get_emp_by_manager(manager_id):
    result = emp_info.get_emp_by_manager(manager_id)

    if type(manager_id) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result



def get_emp_dept(dept_name):
    result = emp_info.get_emp_dept(dept_name)
   
    if type(dept_name) != str:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result


def get_salary_range(start, end):
    result = emp_info.get_salary_range(start, end)

    if type(start) and type(end) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')

    return result

def get_manager_dept(manager_id, dept_no):
    result = emp_info.get_manager_dept(manager_id, dept_no)

    if type(manager_id) != int:
         return jsonify(
            status=400, message='Invalid input.')
    
    if type(dept_no) != str:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result

def get_leaves_employee(emp_no):
    result = emp_info.get_leaves_employee(emp_no)

    if type(emp_no) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result

def get_leaves_taken(emp_no):
    result = emp_info.get_leaves_taken(emp_no)

    if type(emp_no) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result

def leaves_without_pay(emp_no):
    result = emp_info.get_leaves_without_pay(emp_no)

    if type(emp_no) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    return result

def apply_for_leaves(emp_no,applied_leaves):
    taken_leaves = emp_info.get_leaves_taken(emp_no).json
    empty = [str(x) for x in taken_leaves]
    dummy = "".join(empty)
    foul = dummy.strip("[]")
    taken_leave = int(foul)
    left_leaves = emp_info.get_leaves_left(emp_no).json
    empty1 = [str(x) for x in left_leaves]
    dummy1 = "".join(empty1)
    foul1 = dummy1.strip("[]")
    left_leave = int(foul1)
    unpaid_leaves = emp_info.get_leaves_without_pay(emp_no).json
    empty2 = [str(x) for x in unpaid_leaves]
    dummy2 = "".join(empty2)
    foul2 = dummy2.strip("[]")
    unpaid_leave = int(foul2)


    if (left_leave == 0):
        unpaid_leave = unpaid_leave + applied_leaves
        unpaid_leave = emp_info.update_unpaid_leaves(emp_no, unpaid_leave)

    elif(applied_leaves >= 2 and left_leave == 1):
        left_leave = 0
        taken_leave = taken_leave + 1
        unpaid_leave = unpaid_leave + applied_leaves - 1
        unpaid_leave = emp_info.update_unpaid_leaves(emp_no, unpaid_leave)
        taken_leave = emp_info.update_taken_leaves(emp_no, taken_leave)
        left_leave = emp_info.update_left_leaves(emp_no, left_leave)

    
    
    elif(left_leave !=0):
        taken_leave = taken_leave + applied_leaves
        left_leave = left_leave - applied_leaves
        taken_leave = emp_info.update_taken_leaves(emp_no, taken_leave)
        left_leave = emp_info.update_left_leaves(emp_no, left_leave)


def set_employee(emp_no, first_name, last_name, birth_date, gender, hire_date, salary, dept_no):
    result = emp_info.set_employee(emp_no, first_name, last_name, birth_date, gender, hire_date, salary, dept_no)
    datetime.strptime(birth_date, '%Y-%m-%d')
    datetime.strptime(hire_date, '%Y-%m-%d')

    if type(emp_no) != int:
         return jsonify(
            status=400, message='Invalid input.')

    if not result:
         return jsonify(
            status=400,
            message='No such record present')
    
    return result
"""Logic For The Web-App."""
from datetime import datetime

from flask import jsonify

from employee.models import emp_info


def get_emp(emp_no):
    """Get Employee Information."""
    if not emp_no.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    result = emp_info.get_emp(emp_no)

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')

    return result


def get_emp_salary(emp_no):
    """Get Employee Salary."""
    if not emp_no.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    result = emp_info.get_emp_salary(emp_no)

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def get_emp_by_manager(manager_id):
    """Get Employees under a manager."""
    result = emp_info.get_emp_by_manager(manager_id)

    if not manager_id.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def get_emp_dept(dept_name):
    """Get Employees under Single Department."""
    result = emp_info.get_emp_dept(dept_name)

    if not dept_name.isalpha():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def get_salary_range(start, end):
    """Get Employees under salary range."""
    result = emp_info.get_salary_range(start, end)

    if not start.isdigit() and end.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')

    return result


def get_manager_dept(manager_id, dept_no):
    """Get Manager of a department."""
    result = emp_info.get_manager_dept(manager_id, dept_no)

    if not manager_id.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if not dept_no.isalpha():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def get_leaves_employee(emp_no):
    """Get Leaves of the employee."""
    result = emp_info.get_leaves_employee(emp_no)

    if not emp_no.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def get_leaves_taken(emp_no):
    """Get Paid Leaves."""
    result = emp_info.get_leaves_taken(emp_no)

    if not emp_no.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def leaves_without_pay(emp_no):
    """Get Unpaid Leaves."""
    result = emp_info.get_leaves_without_pay(emp_no)

    if not emp_no.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')
    return result


def apply_for_leaves(emp_no, applied_leaves):
    """Apply for Leaves."""
    taken_leaves = emp_info.get_leaves_taken(emp_no).json
    empty = [str(x) for x in taken_leaves]
    dummy = ''.join(empty)
    foul = dummy.strip('[]')
    taken_leave = int(foul)
    left_leaves = emp_info.get_leaves_left(emp_no).json
    empty1 = [str(x) for x in left_leaves]
    dummy1 = ''.join(empty1)
    foul1 = dummy1.strip('[]')
    left_leave = int(foul1)
    unpaid_leaves = emp_info.get_leaves_without_pay(emp_no).json
    empty2 = [str(x) for x in unpaid_leaves]
    dummy2 = ''.join(empty2)
    foul2 = dummy2.strip('[]')
    unpaid_leave = int(foul2)

    if left_leave == 0:
        unpaid_leave = unpaid_leave + applied_leaves
        unpaid_leave = emp_info.update_unpaid_leaves(emp_no, unpaid_leave)

    elif(applied_leaves >= 2 and left_leave == 1):
        left_leave = 0
        taken_leave = taken_leave + 1
        unpaid_leave = unpaid_leave + applied_leaves - 1
        unpaid_leave = emp_info.update_unpaid_leaves(emp_no, unpaid_leave)
        taken_leave = emp_info.update_taken_leaves(emp_no, taken_leave)
        left_leave = emp_info.update_left_leaves(emp_no, left_leave)

    elif left_leave != 0:
        taken_leave = taken_leave + applied_leaves
        left_leave = left_leave - applied_leaves
        taken_leave = emp_info.update_taken_leaves(emp_no, taken_leave)
        left_leave = emp_info.update_left_leaves(emp_no, left_leave)


def set_employee(emp_no, first_name, last_name, birth_date,
                 gender, hire_date, salary, dept_no):
    """Update Employee Function."""
    result = emp_info.set_employee(emp_no, first_name, last_name,
                                   birth_date, gender, hire_date,
                                   salary, dept_no)
    datetime.strptime(birth_date, '%Y-%m-%d')
    datetime.strptime(hire_date, '%Y-%m-%d')

    if not emp_no.isdigit():
        return jsonify(
            status=400, message='Invalid input.')

    if [] in result.values():
        return jsonify(
            status=400,
            message='No such record present')

    return result

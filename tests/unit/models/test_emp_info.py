"""Test Module for Model."""
import pytest

from employee.models import emp_info
from tests.unit import db_utils
from tests.unit.factories.departments import DepartmentsFactory
from tests.unit.factories.dept_manager import Dept_ManagerFactory
from tests.unit.factories.employees import EmployeesFactory
from tests.unit.factories.leaves import LeavesFactory
from tests.unit.factories.salaries import SalariesFactory


@pytest.mark.parametrize(('emp_id'), [1])
@db_utils.test_schema
def test_get_emp(context, emp_id):
    """Test Module for Get Employee Information."""
    db_utils.seed_models(EmployeesFactory.build(emp_no=1))
    with context:
        result = emp_info.get_emp(emp_id)
    assert result.get('emp_id', '1') == [1]


@pytest.mark.parametrize(('emp_id'), [2])
@db_utils.test_schema
def test_get_salary(context, emp_id):
    """Test Module for Get Employee Salary."""
    db_utils.seed_models(SalariesFactory.build(emp_no=2))
    db_utils.seed_models(EmployeesFactory.build(emp_no=2))
    with context:
        result = emp_info.get_emp_salary(emp_id)
    assert result.get('emp_id', '2') == [2]


@pytest.mark.parametrize(('manager_id'), [1])
@db_utils.test_schema
def test_get_manager(context, manager_id):
    """Test Module for Get Employees under a manager."""
    db_utils.seed_models(EmployeesFactory.build(emp_no=1))
    db_utils.seed_models(Dept_ManagerFactory.build(emp_no=1, manager_id=1))
    with context:
        result = emp_info.get_emp_by_manager(manager_id)
    assert result.get('manager_id', '1') == [1]


@pytest.mark.parametrize(('dept_name'), ['IT Services'])
@db_utils.test_schema
def test_get_emp_dept(context, dept_name):
    """Test Module for Get Employees under Single Department."""
    db_utils.seed_models(EmployeesFactory.build(emp_no=1))
    db_utils.seed_models(DepartmentsFactory.build(emp_no=1,
                         dept_name='IT Services'))
    with context:
        result = emp_info.get_emp_dept(dept_name)
    assert result.get('dept_name', 'IT Services') == ['IT Services']


@pytest.mark.parametrize(('start', 'end'), [(100000, 300000)])
@db_utils.test_schema
def test_get_salary_range(context, start, end):
    """Test Module for Get Employees under salary range."""
    db_utils.seed_models(EmployeesFactory.build(emp_no=1))
    db_utils.seed_models(SalariesFactory.build(emp_no=1))
    with context:
        result = emp_info.get_salary_range(start, end)
    assert result.get('emp_id', '1') == [1]


@pytest.mark.parametrize(('manager_id', 'dept_no'), [('1', 'IT')])
@db_utils.test_schema
def test_get_manager_dept(context, manager_id, dept_no):
    """Test Module for Get Manager of a department."""
    db_utils.seed_models(EmployeesFactory.build(emp_no=1))
    db_utils.seed_models(
        Dept_ManagerFactory.build(emp_no=1, manager_id=1, dept_no='IT')
    )
    db_utils.seed_models(DepartmentsFactory.build(emp_no=1, dept_no='IT'))
    with context:
        result = emp_info.get_manager_dept(manager_id, dept_no)
    assert result.get('manager_id', '1') == [1]


@pytest.mark.parametrize(('emp_id'), [2])
@db_utils.test_schema
def test_get_leaves_employee(context, emp_id):
    """Test Module for Get Leaves of the employee."""
    db_utils.seed_models(LeavesFactory.build(emp_no=2))
    db_utils.seed_models(EmployeesFactory.build(emp_no=2))
    with context:
        result = emp_info.get_leaves_employee(emp_id)
    assert result.get('emp_id', '2') == [2]


@pytest.mark.parametrize(('emp_id'), [3])
@db_utils.test_schema
def test_get_leaves_left(context, emp_id):
    """Test Module for Get Leaves Left."""
    db_utils.seed_models(LeavesFactory.build(emp_no=3))
    db_utils.seed_models(EmployeesFactory.build(emp_no=3))
    with context:
        result = emp_info.get_leaves_left(emp_id)
    assert result.get('leaves_left', '1') == [1]


@pytest.mark.parametrize(('emp_id'), [2])
@db_utils.test_schema
def test_get_leaves_taken(context, emp_id):
    """Test Module for Get Paid Leaves."""
    db_utils.seed_models(LeavesFactory.build(emp_no=2))
    db_utils.seed_models(EmployeesFactory.build(emp_no=2))
    with context:
        result = emp_info.get_leaves_taken(emp_id)
    assert result.get('leaves_taken', '2') == [2]


@pytest.mark.parametrize(('emp_id'), [3])
@db_utils.test_schema
def test_get_leaves_without_pay(context, emp_id):
    """Test Module for Get Unpaid Leaves."""
    db_utils.seed_models(LeavesFactory.build(emp_no=3))
    db_utils.seed_models(EmployeesFactory.build(emp_no=3))
    with context:
        result = emp_info.get_leaves_without_pay(emp_id)
    assert result.get('leaves_without_pay', '3') == [3]


@pytest.mark.parametrize(('emp_id', 'unpaid_leaves'), [(3, 3)])
@db_utils.test_schema
def test_update_unpaid_leaves(context, emp_id, unpaid_leaves):
    """Test Module for Update Unpaid Leaves."""
    db_utils.seed_models(LeavesFactory.build(emp_no=3))
    with context:
        result = emp_info.update_unpaid_leaves(emp_id, unpaid_leaves)
    assert result == 'Updated Unpaid Leaves Successfully!!'


@pytest.mark.parametrize(('emp_id', 'taken_leaves'), [(2, 2)])
@db_utils.test_schema
def test_update_taken_leaves(context, emp_id, taken_leaves):
    """Test Module for Update Paid Leaves."""
    db_utils.seed_models(LeavesFactory.build(emp_no=2))
    with context:
        result = emp_info.update_taken_leaves(emp_id, taken_leaves)
    assert result == 'Updated Taken Leaves Successfully!!'


@pytest.mark.parametrize(('emp_id', 'leaves_left'), [(3, 3)])
@db_utils.test_schema
def test_update_left_leaves(context, emp_id, leaves_left):
    """Test Module for Update Leaves Left."""
    db_utils.seed_models(LeavesFactory.build(emp_no=3))
    with context:
        result = emp_info.update_left_leaves(emp_id, leaves_left)
    assert result == 'Updated Leaves Left Successfully!!'


@pytest.mark.parametrize(
    (
        'emp_id',
        'first_name',
        'last_name',
        'birth_date',
        'gender',
        'hire_date',
        'salary',
        'dept_no',
    ),
    [(2, 'Manan', 'Mehta', '1995-07-29', 'M', '2021-10-11', 200000, 'IT')],
)
@db_utils.test_schema
def test_set_employee(
    context,
    emp_id,
    first_name,
    last_name,
    birth_date,
    gender,
    hire_date,
    salary,
    dept_no,
):
    """Test Module for Update Employee Function."""
    db_utils.seed_models(EmployeesFactory.build(emp_no=2))
    db_utils.seed_models(DepartmentsFactory.build(emp_no=2))
    db_utils.seed_models(SalariesFactory.build(emp_no=2))
    with context:
        result = emp_info.set_employee(
            emp_id,
            first_name,
            last_name,
            birth_date,
            gender,
            hire_date,
            salary,
            dept_no,
        )
    assert result == 'Updated Old Employee Record with New Successfully!!'

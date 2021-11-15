import datetime
import decimal
import json
from flask.globals import request

from sqlalchemy.sql.sqltypes import CHAR, VARCHAR, Date

from owsresponse import response
from sqlalchemy import case
from sqlalchemy import Column
from sqlalchemy import DATETIME
from sqlalchemy import Enum
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from employee.connectors import mysql

class Employees(mysql.BaseModel):

    __tablename__ = 'employees'


    emp_no = Column(Integer(11), primary_key=True, nullable=False)
    first_name = Column(VARCHAR(20), nullable=False)
    last_name = Column(VARCHAR(20), nullable=False)
    birth_date = Column(Date(10), nullable=False)
    gender = Column(Enum('M','F'))
    last_updated = Column(DATETIME)


    def __init__(self, emp_no, first_name, last_name, birth_date, gender, last_updated):
        self.emp_no = emp_no
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.last_updated = last_updated


class Salaries(mysql.BaseModel):

    __tablename__ = 'salaries'


    emp_no = Column(Integer(11), primary_key=True, nullable=False)
    salary = Column(Integer(11),primary_key=True, nullable=False)
    from_date = Column(Date(), nullable=False)
    to_date = Column(Date(), nullable=False)


    def __init__(self, emp_no, salary, from_date, to_date):
        self.emp_no = emp_no
        self.salary = salary
        self.from_date = from_date
        self.to = to_date\

class Titles(mysql.BaseModel):

    __tablename__ = 'titles'


    emp_no = Column(Integer(11), primary_key=True, nullable=False)
    title = Column(VARCHAR(50),primary_key=True, nullable=False)
    from_date = Column(Date(),primary_key=True, nullable=False)
    to_date = Column(Date(), nullable=False)


    def __init__(self, emp_no, title, from_date, to_date):
        self.emp_no = emp_no
        self.title = title
        self.from_date = from_date
        self.to = to_date

class Dept_emp(mysql.BaseModel):

    __tablename__ = 'dept_emp'


    emp_no = Column(Integer(11), primary_key=True, nullable=False)
    dept_no = Column(CHAR(4),primary_key=True, nullable=False)
    from_date = Column(Date(), nullable=False)
    to_date = Column(Date(), nullable=False)


    def __init__(self, emp_no, dept_no, from_date, to_date):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.from_date = from_date
        self.to = to_date

class Dept_Manager(mysql.BaseModel):

    __tablename__ = 'dept_manager'


    dept_no = Column(CHAR(4), primary_key=True, nullable=False)
    emp_no = Column(Integer(11),primary_key=True, nullable=False)
    from_date = Column(Date(20), nullable=False)
    to_date = Column(Date(10), nullable=False)


    def __init__(self, emp_no, salary, from_date, to_date):
        self.emp_no = emp_no
        self.salary = salary
        self.from_date = from_date
        self.to = to_date

class Departments(mysql.BaseModel):

    __tablename__ = 'departments'

    dept_no = Column(CHAR(4), primary_key=True, nullable=False)
    dept_name = Column(Integer(11), nullable=False)


    def __init__(self, dept_no, dept_name):
        self.dept_no = dept_no
        self.dept_name = dept_name

class Leaves(mysql.BaseModel):

    __tablename__ = 'leaves'

    emp_no = Column(Integer(11), primary_key=True, nullable=False)
    dept_no = Column(CHAR(4),primary_key=True, nullable=False)
    leaves_taken = Column(Integer(2), primary_key=True)
    leaves_left = Column(Integer(2), primary_key=True)

    def __init__(self, emp_no, dept_no, leaves_taken, leaves_left):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.leaves_taken = leaves_taken
        self.leaves_left = leaves_left

@mysql.wrap_db_errors
def get_emp(emp_id):
     with mysql.db_read_session() as session:
         sql = 'SELECT * \
            FROM employees \
            WHERE emp_no = {employee_id};'.format(employee_id=emp_id)
            emp_response = session.execute(sql)
            result = emp_response.fetchall()
            result_obj = json.loads(json.dumps(result))
            return response.Response(message=result_obj)

@mysql.wrap_db_errors
def get_emp_salary(emp_id, emp_salary):
    with mysql.db_read_session() as session:
        sql = ' SELECT a.emp_no, a.first_name, a.last_name, b.salary, b.from_date, b.to_date \
            FROM  employees a \
            INNER JOIN salaries b \
            ON emp_no = {employee_id} AND salary = {employee_salary};'.format(employee_id=emp_id, employee_salary = emp_salary)
            emp_response = session.execute(sql)
            result = emp_response.fetchall()
            result_obj = json.loads(json.dumps(result))
            return response.Response(message=result_obj)


@mysql.wrap_db_errors
def get_emp_by_manager():
    with mysql.db_read_session() as session:
        sql = ' SELECT a.first_name, a.last_name, b.dept_no, c.first_name, c.last_name, COUNT (b.emp_no) AS number of employees \
        FROM employees a \
        LEFT JOIN  dept_manager b ON a.emp_id = b.emp_id  \
        LEFT JOIN employees c ON b.manager_id = c.emp_id;'
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        result_obj = json.loads(json.dumps(result))
        return response.Response(message=result_obj)


@mysql.wrap_db_errors
def get_emp_dept():
    with mysql.db_read_session() as session:
        sql = 'SELECT e.emp_no, e.first_name, e.last_name, e.birth_date, e.gender, e.hire_date, d.dept_no, d.from_date, d.to_date \
        FROM  employees e, dept_emp d \
        WHERE e.emp_no = d.emp_no;'
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        result_obj = json.loads(json.dumps(result))
        return response.Response(message=result_obj)


@mysql.wrap_db_errors
def get_salary_range(start, end):
    with mysql.db_read_session() as session:
        sql = ' SELECT * FROM employees \
        WHERE salary BETWEEN first = {start} and last = {end};'.format(first=start, last=end) '
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        result_obj = json.loads(json.dumps(result))
        return response.Response(message=result_obj)


'''@mysql.wrap_db_errors
def get_leaves_employee():
    with mysql.db_read_session() as session:
        sql = ' SELECT a.emp_no, a.first_name, a.last_name, b.leaves_taken
        
        '

'''

import datetime
import decimal
import json
from flask.globals import request

from sqlalchemy.sql.sqltypes import CHAR, INTEGER, VARCHAR, Date

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
    hire_date = Column(Date(10))
    last_updated = Column(DATETIME)
    
    
    children_1 = relationship("Salaries", back_populates="parent_1")
    children_2 = relationship("Titles", back_populates="parent_2")
    children_3 = relationship("Dept_Manager", back_populates="parent_3")
    children_4 = relationship("Leaves", back_populates="parent_4")


    def __init__(self, emp_no, first_name, last_name, birth_date, gender, hire_date, last_updated):
        self.emp_no = emp_no
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.gender = gender
        self.hire_date = hire_date
        self.last_updated = last_updated


class Salaries(mysql.BaseModel):

    __tablename__ = 'salaries'


    emp_no = Column(Integer(11), primary_key=True, nullable=False, ForeignKey('employees.emp_no'))
    salary = Column(Integer(11),primary_key=True, nullable=False)
    from_date = Column(Date(), nullable=False)
    to_date = Column(Date(), nullable=False)


    parent_1 = relationship("Employees", back_populates="children_1")


    def __init__(self, emp_no, salary, from_date, to_date):
        self.emp_no = emp_no
        self.salary = salary
        self.from_date = from_date
        self.to = to_date\

class Titles(mysql.BaseModel):

    __tablename__ = 'titles'


    emp_no = Column(Integer(11), primary_key=True, nullable=False, ForeignKey('employees.emp_no'))
    title = Column(VARCHAR(50),primary_key=True, nullable=False)
    from_date = Column(Date() nullable=False)
    to_date = Column(Date(), nullable=False)

    parent_2 = relationship("Employees", back_populates="children_2")


    def __init__(self, emp_no, title, from_date, to_date):
        self.emp_no = emp_no
        self.title = title
        self.from_date = from_date
        self.to = to_date

class Dept_emp(mysql.BaseModel):

    __tablename__ = 'dept_emp'


    emp_no = Column(Integer(11), primary_key=True, nullable=False, ForeignKey('employees.emp_no'))
    dept_no = Column(CHAR(4),primary_key=True, nullable=False, ForeignKey('departments.dept_no'))
    from_date = Column(Date(), nullable=False)
    to_date = Column(Date(), nullable=False)


parent_3 = relationship("Employees", back_populates="children_3")
parent_5 = relationship("Departments", back_populates="children_4")


    def __init__(self, emp_no, dept_no, from_date, to_date):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.from_date = from_date
        self.to = to_date

class Dept_Manager(mysql.BaseModel):

    __tablename__ = 'dept_manager'


    manager_id = Column(Integer(11), primary_key=True, nullable=False)
    dept_no = Column(CHAR(4), primary_key=True, nullable=False, ForeignKey('departments.dept_no'))
    emp_no = Column(Integer(11),primary_key=True, nullable=False)
    from_date = Column(Date(20), nullable=False)
    to_date = Column(Date(10), nullable=False)

    parent_6 = relationship("Departments", back_populates="children_5")


    def __init__(self, manager_id, emp_no, dept_no, from_date, to_date):
        self.manager_id = manager_id
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.from_date = from_date
        self.to_date = to_date

class Departments(mysql.BaseModel):

    __tablename__ = 'departments'

    dept_no = Column(CHAR(4), primary_key=True, nullable=False)
    dept_name = Column(VARCHAR(11), nullable=False)

    children_5 = relationship("Dept_emp", back_populates="parent_4")
    children_6 = relationship("Dept_Manager", back_populates="parent_5")
    children_7 = relationship("Leaves", back_populates="parent_6")


    def __init__(self, dept_no, dept_name):
        self.dept_no = dept_no
        self.dept_name = dept_name

class Leaves(mysql.BaseModel):

    __tablename__ = 'leaves'

    emp_no = Column(Integer(11), primary_key=True, nullable=False), ForeignKey('employees.emp_no')
    dept_no = Column(CHAR(4),primary_key=True, nullable=False, ForeignKey('departments.dept_no'))
    leaves_taken = Column(Integer(2))
    leaves_left = Column(Integer(2))
    leaves_without_pay = Column(Integer(2), primary_key=True)


    parent_4 = relationship("Employees", back_populates="children_4")    
    parent_7 = relationship("Departments", back_populates="children_6")


    def __init__(self, emp_no, dept_no, leaves_taken, leaves_left, leaves_without_pay):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.leaves_taken = leaves_taken
        self.leaves_left = leaves_left
        self.leaves_without_pay = leaves_without_pay

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

from datetime import datetime
from os import uname
from flask.json import jsonify
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
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref, relation, relationship

from employee.connectors import mysql

class Employees(mysql.BaseModel):

    __tablename__ = 'employees'


    emp_no = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(VARCHAR(20), nullable=False)
    last_name = Column(VARCHAR(20), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(Enum('M','F'))
    hire_date = Column(Date, nullable=False)
    last_updated = Column(DATETIME, nullable=False)
    
    
    children_1 = relationship("Salaries", back_populates="parent_1")
    children_2 = relationship('Titles', back_populates="parent_2")
    children_3 = relationship('Leaves', back_populates="parent_3")

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


    emp_no = Column(Integer, ForeignKey('employees.emp_no'), primary_key=True)
    salary = Column(Integer,primary_key=True, nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)


    parent_1 = relationship('Employees', back_populates="children_1")


    def __init__(self, emp_no, salary, from_date, to_date):
        self.emp_no = emp_no
        self.salary = salary
        self.from_date = from_date
        self.to_date = to_date

class Titles(mysql.BaseModel):

    __tablename__ = 'titles'


    emp_no = Column(Integer, ForeignKey('employees.emp_no'), primary_key=True, nullable=False)
    title = Column(VARCHAR(50),primary_key=True, nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    parent_2 = relationship("Employees", back_populates="children_2")



    def __init__(self, emp_no, title, from_date, to_date):
        self.emp_no = emp_no
        self.title = title
        self.from_date = from_date
        self.to_date = to_date

class Dept_Manager(mysql.BaseModel):

    __tablename__ = 'dept_manager'


    manager_id = Column(Integer, primary_key=True, nullable=False)
    dept_no = Column(CHAR(4), ForeignKey('departments.dept_no'),primary_key=True, nullable=False)
    emp_no = Column(Integer,primary_key=True, nullable=False)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    parent_4 = relationship("Departments", back_populates="children_4")


    def __init__(self, manager_id, emp_no, dept_no, from_date, to_date):
        self.manager_id = manager_id
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.from_date = from_date
        self.to_date = to_date

class Departments(mysql.BaseModel):

    __tablename__ = 'departments'

    emp_no = Column(Integer, ForeignKey('employees.emp_no'), primary_key=True, nullable=False)
    dept_no = Column(CHAR(4), primary_key=True, nullable=False)
    dept_name = Column(VARCHAR(11), nullable=False)

    children_4 = relationship('Dept_Manager', back_populates="parent_4")
    children_6 = relationship("Leaves", back_populates="parent_7")


    def __init__(self, emp_no, dept_no, dept_name):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.dept_name = dept_name

class Leaves(mysql.BaseModel):

    __tablename__ = 'leaves'

    emp_no = Column(Integer, ForeignKey('employees.emp_no'), primary_key=True, nullable=False)
    dept_no = Column(CHAR(4), ForeignKey('departments.dept_no'), primary_key=True, nullable=False)
    leaves_taken = Column(Integer)
    leaves_left = Column(Integer)
    leaves_without_pay = Column(Integer, primary_key=True)


    parent_3 = relationship('Employees', back_populates="children_3")    
    parent_7 = relationship('Departments', back_populates="children_6")


    def __init__(self, emp_no, dept_no, leaves_taken, leaves_left, leaves_without_pay):
        self.emp_no = emp_no
        self.dept_no = dept_no
        self.leaves_taken = leaves_taken
        self.leaves_left = leaves_left
        self.leaves_without_pay = leaves_without_pay

@mysql.wrap_db_errors
def get_emp(emp_no):
    with mysql.db_read_session() as session:
        data = dict(emp_id=[], first_name=[], last_name=[], birth_day=[], gender=[], date_hired=[], updated=[])
        sql = 'SELECT * \
            FROM employees \
            WHERE emp_no = {employee_id};'.format(employee_id=emp_no)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['emp_id'].append(results[0])
            data['first_name'].append(results[1])
            data['last_name'].append(results[2])
            data['birth_day'].append(results[3])
            data['gender'].append(results[4])
            data['date_hired'].append(results[5])
            data['updated'].append(results[6])
        return data
        

@mysql.wrap_db_errors
def get_emp_salary(emp_no):
    with mysql.db_read_session() as session:
        data = dict(emp_id=[], first_name=[], last_name=[], salary=[])
        sql = ' SELECT a.emp_no, a.first_name, a.last_name, b.salary \
            FROM  employees a \
            LEFT JOIN salaries b \
            ON a.emp_no = b.emp_no \
            WHERE a.emp_no = {employee_id};'.format(employee_id=emp_no)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['emp_id'].append(results[0])
            data['first_name'].append(results[1])
            data['last_name'].append(results[2])
            data['salary'].append(results[3])
        return data


@mysql.wrap_db_errors
def get_emp_by_manager(manager_id):
    with mysql.db_read_session() as session:
        data = dict(first_name=[], last_name=[], dept_id=[], manager_id=[])
        sql = ' SELECT DISTINCT e.first_name, e.last_name, d.dept_no, d.manager_id \
        FROM employees e \
        LEFT JOIN  dept_manager d \
        ON e.emp_no = d.emp_no \
        GROUP BY d.manager_id \
        HAVING d.manager_id = {manage_id};'.format(manage_id = manager_id)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['first_name'].append(results[0])
            data['last_name'].append(results[1])
            data['dept_id'].append(results[2])
            data['manager_id'].append(results[3])
        return data


@mysql.wrap_db_errors
def get_emp_dept(dept_name):
    with mysql.db_read_session() as session:
        data = dict(emp_id=[], first_name=[], last_name=[], dept_id=[], dept_name=[])
        sql = 'SELECT DISTINCT e.emp_no, e.first_name, e.last_name, d.dept_no, d.dept_name \
        FROM  employees e \
        LEFT JOIN departments d \
        ON e.emp_no = d.emp_no \
        GROUP BY d.dept_name \
        HAVING d.dept_name = "{dept_name}";'.format(dept_name=str(dept_name)) 
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['emp_id'].append(results[0])
            data['first_name'].append(results[1])
            data['last_name'].append(results[2])
            data['dept_id'].append(results[3])
            data['dept_name'].append(results[4])
        return data


@mysql.wrap_db_errors
def get_salary_range(start, end):
    with mysql.db_read_session() as session:
        data = dict(emp_id=[], first_name=[], last_name=[], salary=[])
        sql = ' SELECT a.emp_no, a.first_name, a.last_name, b.salary \
            FROM employees AS a \
            LEFT JOIN salaries AS b ON a.emp_no = b.emp_no \
            WHERE salary BETWEEN {start} and {end};'.format(start=start, end=end)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['emp_id'].append(results[0])
            data['first_name'].append(results[1])
            data['last_name'].append(results[2])
            data['salary'].append(results[3])
        return data


@mysql.wrap_db_errors
def get_manager_dept(manager_id, dept_no):
    with mysql.db_read_session() as session:
        data = dict(first_name=[], last_name=[], manager_id=[], dept_id=[], dept_name=[])
        sql = ' SELECT DISTINCT a.first_name, a.last_name, b.manager_id , b.dept_no, c.dept_name \
            FROM employees a \
            LEFT JOIN dept_manager b \
            ON a.emp_no = b.emp_no \
            LEFT JOIN departments c \
            ON b.emp_no = c.emp_no \
            GROUP BY b.manager_id \
            HAVING b.manager_id = {manager_id} and b.dept_no = "{dept_no}";'.format(manager_id=manager_id, dept_no=str(dept_no))
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['first_name'].append(results[0])
            data['last_name'].append(results[1])
            data['manager_id'].append(results[2])
            data['dept_id'].append(results[3])
            data['dept_name'].append(results[4])
        return data


@mysql.wrap_db_errors
def get_leaves_employee(emp_no):
    with mysql.db_read_session() as session:
        data = dict(emp_id=[], first_name=[], last_name=[], leaves_taken=[], leaves_left=[], unpaid_leaves=[])
        sql = ' SELECT a.emp_no, a.first_name, a.last_name, b.leaves_taken, b.leaves_left, b.leaves_without_pay \
            FROM employees AS a \
            LEFT JOIN leaves AS b ON a.emp_no = b.emp_no \
            WHERE a.emp_no = {emp_no};'.format(emp_no=emp_no)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['emp_id'].append(results[0])
            data['first_name'].append(results[1])
            data['last_name'].append(results[2])
            data['leaves_taken'].append(results[3])
            data['leaves_left'].append(results[4])
            data['unpaid_leaves'].append(results[5])
        return data


@mysql.wrap_db_errors
def get_leaves_left(emp_no):
    with mysql.db_read_session() as session:
        data = dict(leaves_left=[])
        sql = ' SELECT b.leaves_left \
            FROM employees AS a \
            LEFT JOIN leaves AS b ON a.emp_no = b.emp_no \
            WHERE a.emp_no = {emp_no};'.format(emp_no=emp_no)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['leaves_left'].append(results[0])
        return data

@mysql.wrap_db_errors
def get_leaves_taken(emp_no):
    with mysql.db_read_session() as session:
        data = dict(leaves_taken=[])
        sql = ' SELECT b.leaves_taken \
            FROM employees AS a \
            LEFT JOIN leaves AS b ON a.emp_no = b.emp_no \
            WHERE a.emp_no = {emp_no};'.format(emp_no=emp_no)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['leaves_taken'].append(results[0])
        return data

@mysql.wrap_db_errors
def get_leaves_without_pay(emp_no):
    with mysql.db_read_session() as session:
        data = dict(leaves_without_pay=[])
        sql = ' SELECT b.leaves_without_pay \
            FROM employees AS a \
            LEFT JOIN leaves AS b ON a.emp_no = b.emp_no \
            WHERE a.emp_no = {emp_no};'.format(emp_no=emp_no)
        emp_response = session.execute(sql)
        result = emp_response.fetchall()
        for results in result:
            data['leaves_without_pay'].append(results[0])
        return data


@mysql.wrap_db_errors
def update_unpaid_leaves(emp_no, unpaid_leave):
      with mysql.db_read_session() as session:
        # import pdb; pdb.set_trace()
        sql = ' UPDATE leaves \
            SET leaves_without_pay = {unpaid_leave} \
            WHERE emp_no = {emp_no};'.format(emp_no = emp_no, unpaid_leave = unpaid_leave)
        session.execute(sql)
        emp_response = session.commit()
        return "Updated Unpaid Leaves Successfully!!"


@mysql.wrap_db_errors
def update_taken_leaves(emp_no, taken_leave):
      with mysql.db_read_session() as session:
        sql = ' UPDATE leaves \
            SET leaves_taken = {taken_leave} \
            WHERE emp_no = {emp_no};'.format(emp_no = emp_no, taken_leave = taken_leave)
        session.execute(sql)
        emp_response = session.commit()
        return "Updated Taken Leaves Successfully!!"
        

        
@mysql.wrap_db_errors
def update_left_leaves(emp_no, left_leave):
      with mysql.db_read_session() as session:
        sql = ' UPDATE leaves \
            SET leaves_left = {left_leave} \
            WHERE emp_no = {emp_no};'.format(emp_no = emp_no, left_leave = left_leave)
        session.execute(sql)
        emp_response = session.commit()
        return "Updated Leaves Left Successfully!!"



@mysql.wrap_db_errors
def set_employee(emp_no, first_name, last_name, birth_date, gender, hire_date, salary, dept_no):
    with mysql.db_read_session() as session:
        sql1 = ' UPDATE employees \
            SET first_name = "{first_name}", last_name = "{last_name}", birth_date = "{birth_date}", gender = "{gender}", hire_date = "{hire_date}" \
            WHERE emp_no = {emp_no};'.format(emp_no=emp_no, first_name = str(first_name), last_name = str(last_name), birth_date = str(birth_date), gender = str(gender), hire_date = str(hire_date))
        sql2 = ' UPDATE salaries \
            SET salary = {salary}\
            WHERE emp_no = {emp_no};'.format(emp_no=emp_no, salary=salary)
        sql3 = 'UPDATE departments \
            SET dept_no = "{dept_no}"\
            WHERE emp_no ={emp_no};'.format(emp_no=emp_no, dept_no=str(dept_no))
        session.execute(sql1)
        session.execute(sql2)
        session.execute(sql3)
        emp_response = session.commit()
        return "Updated Old Employee Record with New Successfully!!"
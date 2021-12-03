from datetime import date, datetime
import factory
from sqlalchemy import Date
from sqlalchemy.sql.sqltypes import DATETIME
import random

from employee.models.emp_info import Employees


class EmployeesFactory(factory.Factory):

    class Meta:

        model = Employees

    emp_no = factory.Sequence(lambda n: n)
    first_name = factory.Sequence(lambda n: 'first_name' + str(n))
    last_name = factory.Sequence(lambda n: 'last_name' + str(n))
    gender = 'M'
    birth_date = date(random.randint(1947,1999), random.randint(1,12), random.randint(1,30))
    hire_date = date(random.randint(1947,1999), random.randint(1,12), random.randint(1,30))
    last_updated = datetime(random.randint(1947,1999), random.randint(1,12), random.randint(1,30), random.randint(1,12), random.randint(0,59), random.randint(0,59), random.randint(0,78700))
    

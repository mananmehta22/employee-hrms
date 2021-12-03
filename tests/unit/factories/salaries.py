import factory

from employee.models.emp_info import Salaries
from sqlalchemy import Date
from datetime import date, datetime

import random


class SalariesFactory(factory.Factory):

    class Meta:

        model = Salaries

    
    emp_no = factory.Sequence(lambda n: n)
    salary = '200000'
    from_date = date(random.randint(1947,1999), random.randint(1,12), random.randint(1,30))
    to_date = date(random.randint(1947,1999), random.randint(1,12), random.randint(1,30))
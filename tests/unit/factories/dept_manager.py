import factory
from datetime import date
import random

from employee.models.emp_info import Dept_Manager


class Dept_ManagerFactory(factory.Factory):

    class Meta:

        model = Dept_Manager

    manager_id = factory.Sequence(lambda n: n)
    dept_no = factory.Sequence(lambda n: 'dept_no' + str(n))
    emp_no = factory.Sequence(lambda n: n)
    from_date = date(random.randint(1947,1999), random.randint(1,12), random.randint(1,30))
    to_date = date(random.randint(1947,1999), random.randint(1,12), random.randint(1,30))
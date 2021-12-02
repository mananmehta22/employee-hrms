import factory

from employee.models.emp_info import Employees


class EmployeesFactory(factory.Factory):

    class Meta:

        model = Employees

    emp_no = factory.Sequence(lambda n: n)
    first_name = factory.Sequence(lambda n: n)
    last_name = factory.Sequence(lambda n: n)
    birth_date = factory.Sequence(lambda n: n)
    gender = 'M'
    hire_date = factory.Sequence(lambda n: n)
    last_updated = factory.Sequence(lambda n: n)

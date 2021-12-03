import factory

from employee.models.emp_info import Departments


class DepartmentsFactory(factory.Factory):

    class Meta:

        model = Departments

    emp_no = factory.Sequence(lambda n: n)
    dept_no = factory.Sequence(lambda n: 'dept_no' + str(n))
    dept_name = factory.Sequence(lambda n: 'dept_name' + str(n))
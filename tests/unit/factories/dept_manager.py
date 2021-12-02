import factory

from employee.models.emp_info import Dept_Manager


class Dept_ManagerFactory(factory.Factory):

    class Meta:

        model = Dept_Manager

    manager_id = factory.Sequence(lambda n: n)
    dept_no = factory.Sequence(lambda n: n)
    emp_no = factory.Sequence(lambda n: n)
    from_date = factory.Sequence(lambda n: n)
    to_date = factory.Sequence(lambda n: n)
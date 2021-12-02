import factory

from employee.models.emp_info import Leaves


class LeavesFactory(factory.Factory):

    class Meta:

        model = Leaves

    emp_no = factory.Sequence(lambda n: n)
    dept_no = factory.Sequence(lambda n: n)
    leaves_taken = factory.Sequence(lambda n: n)
    leaves_left = factory.Sequence(lambda n: n)
    leaves_without_pay = factory.Sequence(lambda n: n)
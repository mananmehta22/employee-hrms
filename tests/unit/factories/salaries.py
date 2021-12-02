import factory

from employee.models.emp_info import Salaries


class SalariesFactory(factory.Factory):

    class Meta:

        model = Salaries

    emp_no = factory.Sequence(lambda n: n)
    salary = factory.Sequence(lambda n: n)
    from_date = factory.Sequence(lambda n: n)
    to_date = factory.Sequence(lambda n: n)
   
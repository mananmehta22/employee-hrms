"""Factory for the Departments model."""
import factory

from employee.models.emp_info import Departments


class DepartmentsFactory(factory.Factory):
    """Factory for creating Departments instances for testing."""

    class Meta:
        """Meta definition for the Departments factory."""

        model = Departments

    emp_no = factory.Sequence(lambda n: n)
    dept_no = factory.Sequence(lambda n: 'dept_no' + str(n))
    dept_name = factory.Sequence(lambda n: 'dept_name' + str(n))

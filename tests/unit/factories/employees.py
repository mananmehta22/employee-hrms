"""Factory for the Employees model."""
from datetime import date, datetime
import random

import factory

from employee.models.emp_info import Employees


class EmployeesFactory(factory.Factory):
    """Factory for creating Employees instances for testing."""

    class Meta:
        """Meta definition for the Department Manager factory."""

        model = Employees

    emp_no = factory.Sequence(lambda n: n)
    first_name = factory.Sequence(lambda n: 'first_name' + str(n))
    last_name = factory.Sequence(lambda n: 'last_name' + str(n))
    gender = 'M'
    birth_date = date(random.randint(1947, 1999), random.randint(1, 12),
                      random.randint(1, 30))
    hire_date = date(random.randint(1947, 1999), random.randint(1, 12),
                     random.randint(1, 30))
    last_updated = datetime(random.randint(1947, 1999), random.randint(1, 12),
                            random.randint(1, 30), random.randint(1, 12),
                            random.randint(0, 59), random.randint(0, 59),
                            random.randint(0, 78700))

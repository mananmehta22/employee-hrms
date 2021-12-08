"""Factory for the Department Manager model."""
from datetime import date
import random

import factory

from employee.models.emp_info import DeptManager


class Dept_ManagerFactory(factory.Factory):
    """Factory for creating Department Manager instances for testing."""

    class Meta:
        """Meta definition for the Department Manager factory."""

        model = DeptManager

    manager_id = factory.Sequence(lambda n: n)
    dept_no = factory.Sequence(lambda n: 'dept_no' + str(n))
    emp_no = factory.Sequence(lambda n: n)
    from_date = date(random.randint(1947, 1999), random.randint(1, 12),
                     random.randint(1, 30))
    to_date = date(random.randint(1947, 1999), random.randint(1, 12),
                   random.randint(1, 30))

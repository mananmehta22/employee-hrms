"""Factory for the Salaries model."""
from datetime import date
import random

import factory

from employee.models.emp_info import Salaries


class SalariesFactory(factory.Factory):
    """Factory for creating Salaries instances for testing."""

    class Meta:
        """Meta definition for the Department Manager factory."""

        model = Salaries

    emp_no = factory.Sequence(lambda n: n)
    salary = '200000'
    from_date = date(random.randint(1947, 1999), random.randint(1, 12),
                     random.randint(1, 30))
    to_date = date(random.randint(1947, 1999), random.randint(1, 12),
                   random.randint(1, 30))

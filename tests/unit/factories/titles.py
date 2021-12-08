"""Factory for the Titles model."""
import factory

from employee.models.emp_info import Titles


class TitlesFactory(factory.Factory):
    """Factory for creating Titles instances for testing."""

    class Meta:
        """Meta definition for the Department Manager factory."""

        model = Titles

    emp_no = factory.Sequence(lambda n: n)
    title = factory.Sequence(lambda n: n)
    from_date = factory.Sequence(lambda n: n)
    to_date = factory.Sequence(lambda n: n)

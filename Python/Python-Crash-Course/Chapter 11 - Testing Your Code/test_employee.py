import pytest
from employee import Employee


# A decorator
@pytest.fixture
def create_instance():
    """Create an instance of Employee"""
    employee = Employee('hongbo', 'wei', 40000)
    return employee


def test_give_default_raise(create_instance):
    """Test if raising correctly salary by default"""
    create_instance.give_raise()
    assert create_instance.annual_salary == 45000


def test_give_custom_raise(create_instance):
    """Test if raising salary correctly by providing parameter"""
    raise_amount = 6666
    create_instance.give_raise(raise_amount)
    assert create_instance.annual_salary == 46666

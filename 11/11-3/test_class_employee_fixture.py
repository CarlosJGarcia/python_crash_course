import pytest
from class_employee import Employee

@pytest.fixture
def employee():
    """An employee object will be available to all test functions"""
    employee = Employee('Carlos', 'Garcia', 80000)
    return employee

def test_give_default_raise(employee):
    # employee = Employee('Carlos', 'Garcia', 80000)
    employee.give_raise()
    assert employee.annual_salary == 85000    

def test_give_custom_raise(employee):
    # employee = Employee('Carlos', 'Garcia', 80000)
    employee.give_raise(10000)
    assert employee.annual_salary == 90000    
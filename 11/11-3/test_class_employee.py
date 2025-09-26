from class_employee import Employee

def test_give_default_raise():
    employee = Employee('Carlos', 'Garcia', 80000)
    employee.give_raise()
    assert employee.annual_salary == 85000    

def test_give_custom_raise():
    employee = Employee('Carlos', 'Garcia', 80000)
    employee.give_raise(10000)
    assert employee.annual_salary == 90000    
import employee_info as emp

print("Test employee info")

def test_age_range():
    result = emp.get_employees_by_age_range(30, 40)
    test = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert result==test

def test_calculate_average_salary():
    result = emp.calculate_average_salary()
    assert(result == 60166.67) 

def test_get_employees_by_dept():
    test = [
        {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
        {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
    ]
    result = emp.get_employees_by_dept('Sales') 

    assert(result==test)  # Assuming the expected result is correct, adjust as per your data  
    
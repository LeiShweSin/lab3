import employee_info as emp

print("Test employee info")

def test_age_range():
    result = emp.get_employees_by_age_range(30, 40)
    test = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert result==test

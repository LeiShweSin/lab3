import lab2.bmi as bmi
print("Test Lab2 BMI")

def test_bmi_normal_weight():
    bmi_calculated = bmi.calculate_bmi(1.73,60)
    result = bmi.classify_bmi(bmi_calculated)
    test = 0
    assert(result==test)

def test_bmi_over_weight():
    bmi_calculated = bmi.calculate_bmi(1.73,85)
    result = bmi.classify_bmi(bmi_calculated)
    test = 1
    assert(result==test)

def test_bmi_under_weight():
    bmi_calculated = bmi.calculate_bmi(1.73,50)
    result = bmi.classify_bmi(bmi_calculated)
    test = -1
    assert(result==test)
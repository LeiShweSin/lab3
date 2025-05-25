import lab2.exe2lab2 as lab2

print("Lab 2 Test")

def test_find_min_max():
    input = [10, 12.5, 20.3, 15.8, 18.2]
    result = lab2.calc_min_max_temperature(input)
    test = [10, 20.3]
    assert(result==test)

def test_calc_avg():
    input = [10, 12.5, 20.3, 15.8, 18.2]
    result = lab2.calc_average_temperature(input)
    test = 15.36
    assert(result==test)

def test_calc_median_odd():
    input = [10, 12.5, 20.3, 15.8, 18.2]
    sort = lab2.sort_temperature(input)
    result = lab2.calc_median_temperature(sort)
    test = 15.8
    assert(result==test)

def test_calc_median_even():
    input = [10, 12.5, 20.3, 15.8]
    sort = lab2.sort_temperature(input)
    result = lab2.calc_median_temperature(sort)
    test = 14.15
    assert(result==test)

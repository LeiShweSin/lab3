import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def test_bubble_sort_morethan10():
    input_arr = [23,45,67,89,12,23,35,56,90,12,13]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = 1
    assert (result==test)

def test_bubble_sort_equalto10():
    input_arr = [23,45,67,89,12,23,35,56,90,12]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = 1
    assert (result==test)

def test_bubble_sort_zero():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = 0
    assert (result==test)

def test_bubble_sort_not_int():
    input_arr = ["i", "don't", "like", "this"]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    test = 2
    assert (result==test)
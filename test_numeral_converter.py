from numeral_converter import NumeralConverter

def test_validations():
    assert nc._N_valid('a') == False
    assert nc._N_valid(0.5) == False
    assert nc._N_valid(-1) == False
    assert nc._N_valid(0) == True
    assert nc._N_valid(55) == True
    assert nc._base_valid('a') == False
    assert nc._base_valid(0.5) == False
    assert nc._base_valid(-1) == False
    assert nc._base_valid(0) == False
    assert nc._base_valid(1) == False
    assert nc._base_valid(2) == True
    assert nc._base_valid(55) == True
    assert nc._digits_valid(1, [0, 0, 0]) == False
    assert nc._digits_valid(3, 'a') == False
    assert nc._digits_valid(3, 1) == False
    assert nc._digits_valid(3, []) == False
    assert nc._digits_valid(3, [-1, -1]) == False
    assert nc._digits_valid(3, [3, 3]) == False
    assert nc._digits_valid(3, [8, 8]) == False
    assert nc._digits_valid(3, [0, 2.1]) == False
    assert nc._digits_valid(3, [0, 2]) == True
    assert nc._digits_valid(121, [0, 45, 7, 120]) == True

def test_functionality():
    a = nc.get_value(2, [1, 0, 1])
    assert a == 5
    a = nc.get_value(7, [6, 0, 2, 5])
    assert a == 2077
    a = nc.convert_to_base(2, 5)
    assert a == [1, 0, 1]
    a = nc.convert_to_base(7, 2077)
    assert a == [6, 0, 2, 5]
    a = nc.get_value(29, [4, 19, 28, 1, 13, 7])
    assert a == 96167052
    a = nc.convert_to_base(29, 96167052)
    assert a == [4, 19, 28, 1, 13, 7]
    a = nc.get_value(31, [3, 11, 4, 1, 23, 30])
    assert a == 96167052
    a = nc.convert_to_base(31, 96167052)
    assert a == [3, 11, 4, 1, 23, 30]
    a = nc.get_value(823, [217, 556, 791, 452, 208])
    assert a == 99864556372192
    a = nc.convert_to_base(823, 99864556372192)
    assert a == [217, 556, 791, 452, 208]
    a = nc.get_value(79, [2, 0, 11, 17, 0])
    assert a == 77970156
    a = nc.convert_to_base(79, 77970156)
    assert a == [2, 0, 11, 17, 0]

nc = NumeralConverter()
test_validations()
test_functionality()


from mixed_radix_numeral_converter import MixedRadixNumeralConverter

def test_validations():
    assert mrnc._N_valid('a') == False
    assert mrnc._N_valid(0.5) == False
    assert mrnc._N_valid(-1) == False
    assert mrnc._N_valid(0) == True
    assert mrnc._N_valid(55) == True

    assert mrnc._bases_valid(1) == False
    assert mrnc._bases_valid(['a', 2]) == False
    assert mrnc._bases_valid([0.5, 2]) == False
    assert mrnc._bases_valid([-1, 2]) == False
    assert mrnc._bases_valid([0, 2]) == False
    assert mrnc._bases_valid([1, 2]) == True
    assert mrnc._bases_valid([1, 1]) == False
    assert mrnc._bases_valid([1, 1, 1, 1, 1, 1]) == False
    assert mrnc._bases_valid([1, 1, 1, 1, 1, 1, 1, 2, 1, 1]) == True
    assert mrnc._bases_valid([3, 4, 5, 6, 7, 8]) == True
    assert mrnc._bases_valid([823, 4, 1, 273617]) == True

    assert mrnc._bases_digits_valid(bases=[], digits=[1]) == False
    assert mrnc._bases_digits_valid(bases=[1, 1], digits=[0, 0, 0]) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=1) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=['a', 0, 1]) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=[-1, 0, 1]) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=[1.5, 0, 1]) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=[1, 0]) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=[1, 0, 0, 0]) == False
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=[1, 2, 2]) == False
    assert mrnc._bases_digits_valid(bases=[3], digits=[1, 5]) == False
    assert mrnc._bases_digits_valid(bases=[3], digits=[5, 1]) == True
    assert mrnc._bases_digits_valid(bases=[3, 2], digits=[1, 0, 1]) == True
    assert mrnc._bases_digits_valid(bases=[823, 3, 2], digits=[983721, 721, 2, 1]) == True


def test_functionality():
    a = mrnc.get_value(bases=[4, 7, 16, 10], digits=[4, 2, 3, 11, 8])
    assert a == 20758
    a = mrnc.convert_to_base(bases=[4, 7, 16, 10], N=20758)
    assert a == [4, 2, 3, 11, 8]

    a = mrnc.get_value(bases=[24, 60, 60, 100], digits=[421, 23, 57, 23, 87])
    assert a == 3646064387
    a = mrnc.convert_to_base(bases=[24, 60, 60, 100], N=3646064387)
    assert a == [421, 23, 57, 23, 87]

    a = mrnc.get_value(bases=[60, 60], digits=[100, 59, 59])
    assert a == 363599
    a = mrnc.convert_to_base(bases=[60, 60], N=363599)
    assert a == [100, 59, 59]

    a = mrnc.get_value(bases=[823, 823, 823, 823], digits=[217, 556, 791, 452, 208])
    assert a == 99864556372192
    a = mrnc.convert_to_base(bases=[823, 823, 823, 823], N=99864556372192)
    assert a == [217, 556, 791, 452, 208]

mrnc = MixedRadixNumeralConverter()
test_validations()
test_functionality()

for i in range(30):
    a = mrnc.convert_to_base(bases=[5, 3, 2], N=i)
    print(a)

for i1 in range(5):
    for i2 in range(3):
        for i3 in range(2):
            a = mrnc.get_value(bases=[5, 3, 2], digits=[0, i1, i2, i3])
            print(a)


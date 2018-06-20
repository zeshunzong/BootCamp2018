# test_solutions.py
"""Volume 1B: Testing.
<Name>
<Class>
<Date>
"""

import solutions as soln
import pytest

# Problem 1: Test the addition and fibonacci functions from solutions.py
def test_addition():
    assert soln.addition(1,2) == 3

def test_smallest_factor():
    assert soln.smallest_factor(1)==1, "when n = 1"
    assert soln.smallest_factor(2)==2, "when n = 2"
    assert soln.smallest_factor(3)==3, "when n = 3"
    assert soln.smallest_factor(4)==2, "when n = 4"
    assert soln.smallest_factor(6)==2, "when n = 6"

def test_month_length():
    assert soln.month_length("January") == 31, "in Jan"
    assert soln.month_length("February", True) == 29, "in Feb, leap year"
    assert soln.month_length("February", False) == 28, "in Feb, not leap year"
    assert soln.month_length("April") == 30, "in April"
    assert soln.month_length("AAAA") == None, "when invalid input"

# Problem 2: Test the operator function from solutions.py
def test_operator():
    #test good cases
    assert soln.operator(2,1, "+") == 3, "plus"
    assert soln.operator(2,1, "-") == 1, "minus"
    assert soln.operator(2,1, "*") == 2, "multiply"
    assert soln.operator(2,1, "/") == 2, "divide"
    #test exceptions
    with pytest.raises(ValueError) as excinfo:
        soln.operator(4, 0, "/")
    assert excinfo.value.args[0] == "You can't divide by zero!"

    with pytest.raises(ValueError) as excinfo:
        soln.operator(4, 0, 1)
    assert excinfo.value.args[0] == "Oper should be a string"

    with pytest.raises(ValueError) as excinfo:
        soln.operator(4, 0, "**")
    assert excinfo.value.args[0] == "Oper should be one character"

    with pytest.raises(ValueError) as excinfo:
        soln.operator(4, 0, "!")
    assert excinfo.value.args[0] == "Oper can only be: '+', '/', '-', or '*'"
'''
# Problem 3: Finish testing the complex number class
#@pytest.fixture
#def set_up_complex_nums():
    number_1 = soln.ComplexNumber(1, 2)
    number_2 = soln.ComplexNumber(5, 5)
    number_3 = soln.ComplexNumber(2, 9)
    return number_1, number_2, number_3

#def test_complex_addition(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 + number_2 == soln.ComplexNumber(6, 7)
    assert number_1 + number_3 == soln.ComplexNumber(3, 11)
    assert number_2 + number_3 == soln.ComplexNumber(7, 14)
    assert number_3 + number_3 == soln.ComplexNumber(4, 18)

def test_complex_multiplication(set_up_complex_nums):
    number_1, number_2, number_3 = set_up_complex_nums
    assert number_1 * number_2 == soln.ComplexNumber(-5, 15)
    assert number_1 * number_3 == soln.ComplexNumber(-16, 13)
    assert number_2 * number_3 == soln.ComplexNumber(-35, 55)
    assert number_3 * number_3 == soln.ComplexNumber(-77, 36)

# Problem 4: Write test cases for the Set game.


@pytest.fixture
def set_up_fractions():
    frac_1_3 = specs.Fraction(1, 3)
    frac_1_2 = specs.Fraction(1, 2)
    frac_n2_3 = specs.Fraction(-2, 3)
    return frac_1_3, frac_1_2, frac_n2_3

def test_fraction_init(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_3.numer == 1
    assert frac_1_2.denom == 2
    assert frac_n2_3.numer == -2
    frac = specs.Fraction(30, 42) # 30/42 reduces to 5/7.
    assert frac.numer == 5
    assert frac.denom == 7

def test_fraction_str(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert str(frac_1_3) == "1/3"
    assert str(frac_1_2) == "1/2"
    assert str(frac_n2_3) == "-2/3"

def test_fraction_float(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert float(frac_1_3) == 1 / 3.
    assert float(frac_1_2) == .5
    assert float(frac_n2_3) == -2 / 3.

def test_fraction_eq(set_up_fractions):
    frac_1_3, frac_1_2, frac_n2_3 = set_up_fractions
    assert frac_1_2 == specs.Fraction(1, 2)
    assert frac_1_3 == specs.Fraction(2, 6)
    assert frac_n2_3 == specs.Fraction(8, -12)
'''

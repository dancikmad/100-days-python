import pytest
from ...day3.exercise import calculate_bmi, bmi_calculator_interpretation


@pytest.fixture
def get_bmi_value():
    weight = 85
    height = 1.85
    bmi = calculate_bmi(weight, height)

    return bmi


def test_bmi_interpretation(get_bmi_value):
    interpretation = bmi_calculator_interpretation(get_bmi_value)

    assert interpretation == "normal weight"
    assert interpretation != "underweight"
    assert interpretation != "overweight"


def test_bmi_low_value():
    assert calculate_bmi(40, 1.8) < 18.5


def test_bmi_high_value():
    assert calculate_bmi(150, 1.6) > 30


# tests for raise an error when heighjt is zero or negative
def test_bmi_zero_height():
    with pytest.raises(ValueError, match="Height must be greater than zero"):
        calculate_bmi(70, 0)


def test_bmi_negative_height():
    with pytest.raises(ValueError, match="Height must be greater than zero"):
        calculate_bmi(70, -1.75)


# tests to ensure correct classification for values at category boundaries
def test_bmi_exact_underweight():
    assert bmi_calculator_interpretation(18.4) == "underweight"


def test_bmi_exact_normal_weight():
    assert bmi_calculator_interpretation(18.5) == "normal weight"


def test_bmi_exact_overweight():
    assert bmi_calculator_interpretation(25.0) == "overweight"


# tests for invalid inputs
def test_bmi_invalid_string():
    with pytest.raises(ValueError, match="BMI must be an integer or float"):
        bmi_calculator_interpretation("twenty")


def test_bmi_invalid_list():
    with pytest.raises(ValueError, match="BMI must be an integer or float"):
        bmi_calculator_interpretation([22])


# tests for `calculate_bmi` raises an error for incorrect data types
def test_bmi_invalid_weight():
    with pytest.raises(TypeError):
        calculate_bmi("seventy", 1.75)


def test_bmi_invalid_height():
    with pytest.raises(TypeError):
        calculate_bmi(70, "one point seven five")


# test for floating point precision
def test_bmi_precision():
    bmi = calculate_bmi(70, 1.75)
    expected_bmi = 70 / (1.75**2)
    assert round(bmi, 2) == round(expected_bmi, 2)


# tests for very small and very large heights
def test_bmi_very_small_height():
    bmi = calculate_bmi(70, 0.5)  # Very short person
    assert bmi > 50


def test_bmi_very_large_height():
    bmi = calculate_bmi(70, 3.0)
    assert bmi < 10

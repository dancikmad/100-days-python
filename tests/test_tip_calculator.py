import pytest
from ..day2_data_types.tip_calculator import TipCalculator  # type: ignore


@pytest.fixture
def tip_calculator():
    return TipCalculator(100, 12, 3)


def test_tip_calculator_raises_exception_on_zero_people():
    with pytest.raises(ValueError):
        TipCalculator(100, 12, 0)


def test_for_negative_values():
    with pytest.raises(ValueError):
        TipCalculator(-1, 12, 3)


def test_calculate_final_amount(tip_calculator):
    final_amount = tip_calculator.calculate_final_amount()
    assert final_amount == 37.33


def test_tip_calculator_attributes(tip_calculator):
    # Check the initial attributes
    assert tip_calculator.bill == 100
    assert tip_calculator.tip == 12
    assert tip_calculator.people == 3
    assert tip_calculator.tip_as_percent == 0.12  # 12 % converted to decimal

    # Check the computed attributes
    assert tip_calculator.total_bill == 112  # 100 + 12% of 100 == 100 + 12 = 112
    assert tip_calculator.bill_per_person == pytest.approx(
        37.33, rel=1e-2
    )  # 112 / 13 approx. 8.615

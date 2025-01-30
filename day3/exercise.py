from typing import Union

def bmi_calculator_interpretation(bmi: Union[int, float]) -> str:
    if not isinstance(bmi, (int, float)):
        raise ValueError("BMI must be an integer or float")

    match bmi:
        case _ if bmi < 18.5:
            return "underweight"
        case _ if 18.5 <= bmi < 25:
            return "normal weight"
        case _ if bmi >= 25:
            return "overweight"

def calculate_bmi(weight: Union[int, float], height: Union[int, float]) -> float:
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    return weight / (height ** 2)

weight = 85
height = 1.85
bmi = calculate_bmi(weight, height)
print(bmi)
bmi_interpretation = bmi_calculator_interpretation(bmi)
print(bmi_interpretation)
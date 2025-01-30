from typing import Union
from colorama import Fore, Back, Style, init

init(autoreset=True)  # Ensures colors reset after each print


class TipCalculator:
    def __init__(self, bill: float, tip: int, people: int):
        if bill < 0 or tip < 0 or people < 0:
            raise ValueError("Bill, tip, and people must be non-negative values.")
        if people == 0:
            raise ValueError("Number of people cannot be zero.")

        self.bill = bill
        self.tip = tip
        self.people = people
        self.tip_as_percent = tip / 100
        self.total_bill = self._calculate_total_bill()
        self.bill_per_person = self._split_bill_per_person()

    def _calculate_total_tip_amount(self) -> Union[int, float]:
        return self.bill * self.tip_as_percent

    def _calculate_total_bill(self) -> Union[int, float]:
        return self.bill + self._calculate_total_tip_amount()

    def _split_bill_per_person(self) -> Union[int, float]:
        return self.total_bill / self.people

    def calculate_final_amount(self) -> Union[int, float]:
        return round(self.bill_per_person, 2)


if __name__ == "__main__":
    while True:
        launch = input(
            Fore.GREEN
            + "Press "
            + Back.WHITE
            + Fore.BLACK
            + " Enter "
            + Style.RESET_ALL
            + Fore.GREEN
            + " to run the final project you built or type 'q' to quit: "
            + Style.RESET_ALL
        )

        if launch.lower() == "q":
            print(Fore.YELLOW + "Goodbye! Have a great day! 😊" + Style.RESET_ALL)
            break

        try:
            bill = float(input("What was the total bill: $ "))
            tip = int(
                input("What percentage tip would you like to give (e.g., 10, 12, 15): ")
            )
            people = int(input("How many people to split the bill: "))

            calculator = TipCalculator(bill, tip, people)
            final_amount = calculator.calculate_final_amount()

            print(
                Fore.CYAN
                + f"Each person should pay: ${final_amount:.2f}"
                + Style.RESET_ALL
            )

        except ValueError:
            print(
                Fore.RED
                + "Invalid input! Please enter a valid number."
                + Style.RESET_ALL
            )

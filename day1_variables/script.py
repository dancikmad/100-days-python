import time
from colorama import Fore, Style, Back

def generate_band_name() -> None:
    """
    Generates a band name based on the user's input.

    This function prompts the user to press Enter to begin. Once the user presses Enter,
    it introduces the Band Name Generator and asks the user to input two pieces of information:
    the city they grew up in and the name of a pet. Based on these inputs, the function generates
    a band name by combining the city and pet name and displays the result.

    It also utilizes `colorama` to print a message in green when asking the user to press Enter,
    and resets the color after the message is displayed.

    Args:
        None

    Returns:
        None
    """
    while True:
        launch = input(Fore.GREEN + "Press " + Back.WHITE + Fore.BLACK + " Enter " + Style.RESET_ALL + Fore.GREEN + " to run the final project you build or type 'q' to quit: " + Style.RESET_ALL)
        
        if launch.lower() == 'q':
            print(Style.RESET_ALL, end="")
            break
        print(Style.RESET_ALL, end="")
        print("Welcome to the Band Name Generator.")
        time.sleep(1)
        city_prompt = input("Which city did you grow up in?\n: ")
        pet_prompt = input("What is the name of a pet?\n: ")

        if city_prompt and pet_prompt:
            print("Your band name could be " + city_prompt + " " + pet_prompt)
        else:
            print("Both inputs are required. Please try again.")

if __name__ == "__main__":
    generate_band_name()
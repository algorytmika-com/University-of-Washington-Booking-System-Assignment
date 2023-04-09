import pandas as pd
from utils import input_validation as iv
from utils import business_validation as bv

def get_booking_max_id(bookings : pd.DataFrame) -> int:
    return bookings['booking_id'].max()

def get_input_consumer_name() -> str:
    return get_input("Enter the name:", 'full_name', "Minimum 5 letters.")

def is_international() -> bool:
    input = get_input("International destination?:", 'true_false', "[Y/N]")
    if input.lower() == 'y':
        return True
    else:
        return False

def get_destination_country() -> str:
    if is_international():
        destination_country = get_input("What is the destination country?:", 'destination_country', "Minimum 5 letters.")
    else:
        destination_country = 'United States of America' 
    return destination_country   

def get_package_description() -> str:
    return get_input("Enter the package description:", 'description', "Minimum 3 letters.")  
       
def is_dangerous() -> bool:
    input = get_input("Are the contents dangerous? [Y/N]:", 'true_false', "[Y/N]")
    if input.lower() == 'y':
        return True
    else:
        return False   

def get_input_weight() -> float:
    while True:
        input = get_input("Enter the weight in kgs:", 'weight', "Positive float value (e.g. 7.25)") 
        try:
            weight = float(input)
        except ValueError:
            print("The weight is not of float type.")
        is_business_validated = bv.is_weight_business_rule(weight, "Packages can only be shipped if they weigh less than 10Kg.")
        if is_exit_from_procedure(is_business_validated):
            return -1
        else:
            continue
    return weight

def get_input(prompt, validation_option, format) -> str:
    while True:
        result = input(f"{prompt} ")
        if iv.is_valid(result, validation_option):
            break
        else:
            print(f"""The inserted value is not correct. 
            The proper format is: {format}
            Please enter again: """)
            continue
    return result

def is_exit_from_procedure(is_validated) -> bool:
    if is_validated:
        return False
    else:
        input = get_input("Do you want to end the booking procedure? [Y/N]:", 'true_false', "[Y/N]")
        if input.lower() == 'y':
            return True
        else:
            return False




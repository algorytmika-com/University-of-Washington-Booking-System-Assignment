import pandas as pd
from utils import validation as v

def get_booking_max_id(bookings : pd.DataFrame) -> int:
    return bookings['booking_id'].max()

def get_input_consumer_name() -> str:
    return get_input("Enter the name:", 'full_name', "No comma, minimum 5 letters.")

def is_international() -> bool:
    input = get_input("International destination?:", 'true_false', "[Y/N]")
    if input.lower() == 'y':
        return True
    else:
        return False

def get_destination_country() -> str:
    if is_international():
        destination_country = get_input("What is the destination country?:", 'destination_country', "No comma, minimum 5 letters.")
    else:
        destination_country = 'United States of America' 
    return destination_country   

    

def get_input(prompt, validation_option, format):
    while True:
        result = input(f"{prompt} ")
        if v.is_valid(result, validation_option):
            break
        else:
            print(f"""The inserted value is not correct. 
            The proper format is {format}
            Please enter again: """)
            continue
    return result




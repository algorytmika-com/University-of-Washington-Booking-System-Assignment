import pandas as pd
from utils import input_validation as iv
from utils import business_validation as bv
from models import booking as b, route as r


POSITIVE_FLOAT = "Positive float value (e.g. 7.25)"

def get_booking_max_id(bookings : pd.DataFrame) -> int:
    return bookings['booking_id'].max()

def get_input_customer_name() -> str:
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
    
def is_urgent() -> bool:
    input = get_input("Is urgent? [Y/N]:", 'true_false', "[Y/N]")
    if input.lower() == 'y':
        return True
    else:
        return False     

def get_input_weight() -> float:
    return get_input_with_business_validation("weight", "Enter the weight in kgs [max 10]:", 'positive_float', POSITIVE_FLOAT)

def get_input_volume() -> float:
    width = get_input_with_business_validation("dimension", "Enter the width in meters [max 5] :", 'positive_float', POSITIVE_FLOAT)
    if width == -1:
        return -1
    height = get_input_with_business_validation("dimension", "Enter the height in meters [max 5] :", 'positive_float', POSITIVE_FLOAT)
    if height == -1:
        return -1    
    depth = get_input_with_business_validation("dimension", "Enter the depth in meters [max 5] :", 'positive_float', POSITIVE_FLOAT)
    if depth == -1:
        return -1
    volume = width * depth * height
    return volume

def get_required_date():
    input = get_input("What is the required delivery date (month/date/year):", 'future_date', "Future date (month/date/year)")
    return input

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
        
def get_input_with_business_validation(business_validation_option, prompt, input_validation_option, format):
    while True:
        input = get_input(prompt, input_validation_option, format) 
        try:
            value = float(input)
        except ValueError:
            print("The value is not of float type.")
        is_business_validated = bv.is_valid(value, business_validation_option)
        if is_business_validated:
            return value
        else:
            if is_exit_from_procedure(is_business_validated):
                return -1
            else:
                continue    

def get_route(customer_booking : b.Booking) -> r.Route:
    route = r.Route(is_ground = True, is_air = True, is_ocean = True)
    route.set_preferred_route(route.GROUND)
    if not bv.is_international(customer_booking):
        route.set_ocean_route(False)
    if bv.is_urgent(customer_booking):
        route.set_preferred_route(route.AIR)
    if bv.is_dangerous(customer_booking):
        route.set_air_route(False)
    if (bv.is_heavy(customer_booking) or bv.is_large(customer_booking)) and not bv.is_urgent(customer_booking):
        if bv.is_international(customer_booking):
            route.set_preferred_route(route.OCEAN)
        else:
            route.set_preferred_route(route.GROUND)
    return route

        



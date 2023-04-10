import pandas as pd
from utils import input_validation as iv
from utils import business_validation as bv
from utils import date_utils as d
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

def get_required_date(is_urgent: bool):
    input = get_input("What is the required delivery date (month/date/year):", 'future_date', "Future date (month/date/year)")
    if is_urgent:
        print("The package is urgent - the date set to 3 days from now.")
        return d.convert_datetime_to_str(d.add_date(days_added = 3), '%m/%d/%Y')
    else:
        if d.get_date_converted_from_str(input, '%m/%d/%Y') > d.add_date(days_added = 7):
            return input
        else:
            print("The package is not urgent - the delivery date cannot be set to less than 7 days from now.")
            return d.convert_datetime_to_str(d.add_date(days_added = 7), '%m/%d/%Y')

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
    route = r.Route(is_air= True, is_ground= True, is_ocean= True)
    route.set_preferred_route(route.GROUND)
    print('route.preferred_route= ', route.preferred_route)
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
    print('route.is_air= ', route.is_air)
    return route

def get_route_prices(customer_booking : b.Booking) -> r.Route:
    route = customer_booking.route
    route.set_ground_price(get_ground_cost(customer_booking))
    route.set_air_price(get_air_cost(customer_booking))
    route.set_ocean_price(get_ocean_cost(customer_booking))
    return route

def get_air_cost(customer_booking : b.Booking) -> float:
    air_weight_cost = customer_booking.weight * 10
    air_volume_cost = customer_booking.volume * 20
    if customer_booking.route.is_air:
        if air_volume_cost >= air_weight_cost:
            return round(air_volume_cost, 2)
        else:
            return round(air_weight_cost, 2)
    else:
        return -1

def get_ground_cost(customer_booking : b.Booking) -> float:
    if customer_booking.route.is_ground:
        if customer_booking.is_urgent:
            return 45
        else:
            return 25
    else:
        return -1
    
def get_ocean_cost(customer_booking : b.Booking) -> float:
    if customer_booking.route.is_ocean:
        return 30
    else:
        return -1

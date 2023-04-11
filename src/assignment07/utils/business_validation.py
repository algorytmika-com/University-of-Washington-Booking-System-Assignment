from cerberus import Validator
from models import booking
from utils import date_utils as d

def is_valid(value, option):
    if option == 'weight':
        return is_weight_business_rule(value)
    elif option == 'dimension':
        return is_dimension_business_rule(value)    
    else:
        print("The validation option not exists!!!")
        return False

def is_weight_business_rule(weight : float) -> bool:
    if weight > 0 and weight <= 10:
        return True
    else:
        print("The weight is too big. Packages can only be shipped if they weigh less than 10Kg.")
        return False
    
def is_dimension_business_rule(weight : float) -> bool:
    if weight > 0 and weight <= 5:
        return True
    else:
        print("The dimension is too big. Packages can only be shipped if they smaller than 5x5x5 meters (125 cubic meters).")
        return False
    
def is_dangerous(booking_obj: booking.Booking) -> bool:
    return booking_obj.is_dangerous

def is_urgent(booking_obj: booking.Booking) -> bool:
    return booking_obj.is_urgent
   
def is_rule_for_urgent(booking_obj: booking.Booking) -> bool:
    future_date = d.get_date_converted_from_str(booking_obj.required_delivery_date, '%m/%d/%Y')
    if booking_obj.is_urgent and d.is_date_in_future_days(future_date, 3):
        return True
    else:
        return False
    
def is_possible_to_route_urgent_via_air(booking_obj: booking.Booking) -> bool:
    if booking_obj.is_urgent and booking_obj.is_dangerous:
        return False
    else: 
        return True

def is_heavy(booking_obj: booking.Booking) -> bool:
    if booking_obj.weight > (booking_obj.weight * 0.8):
        return True
    else:
        return False
    
def is_large(booking_obj: booking.Booking) -> bool:
    if booking_obj.volume > (booking_obj.volume * 0.8):
        return True
    else:
        return False
    
def is_international(booking_obj: booking.Booking) -> bool:
    if booking_obj.destination_country != "United States of America":
        return True
    else:
        return True
    

    
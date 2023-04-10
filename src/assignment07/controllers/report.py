import pandas as pd

from models import booking as b
from utils import format as f

def convert_to_dataframe(booking_obj : b.Booking) -> pd.DataFrame:
    d = {'customer_name' : [booking_obj.customer_name],
         'destination_country' : [booking_obj.destination_country],
         'package_description' : [booking_obj.package_description],
         'weight' : [booking_obj.weight],
         'volume' : [booking_obj.volume],
         'is_dangerous' : [booking_obj.is_dangerous],
         'is_urgent' : [booking_obj.is_urgent],
         'air_price' : [booking_obj.route.air_price], 
         'ground_price' : [booking_obj.route.ground_price],
         'ocean_price' : [booking_obj.route.ocean_price]
         }
    return pd.DataFrame(data=d)

def print_all_bookings(booking: pd.DataFrame, title):
    print_shipping_options(booking, title)

def print_urgent_bookings(booking: pd.DataFrame, title):
    booking = booking[booking['is_urgent'] == True]
    print_shipping_options(booking, title)    

def print_dangerous_bookings(booking: pd.DataFrame, title):
    booking = booking[booking['is_dangerous'] == True]
    print_shipping_options(booking, title)        

def print_shipping_options(booking: pd.DataFrame, title):
    f.print_message(title)
    booking = booking.astype({'air_price':'string','ground_price':'string', 'ocean_price':'string'})
    booking['destination_country'] = booking['destination_country'].str[:24]
    booking['package_description'] = booking['package_description'].str[:24]
    booking['ground_price'] = '$' + booking['ground_price']
    booking['air_price'] = '$' + booking['air_price']
    booking['ocean_price'] = '$' + booking['ocean_price']
    booking['air_price'] = booking['air_price'].replace(['$-1.0'], '-') 
    booking['ground_price'] = booking['ground_price'].replace(['$-1.0'], '-')    
    booking['ocean_price'] = booking['ocean_price'].replace(['$-1.0'], '-') 
    booking['air_price'] = booking['air_price'].replace(['$-1'], '-') 
    booking['ground_price'] = booking['ground_price'].replace(['$-1'], '-')    
    booking['ocean_price'] = booking['ocean_price'].replace(['$-1'], '-')     
    print(booking[['customer_name','destination_country','package_description','weight', 'volume','is_dangerous', 'is_urgent', 'air_price', 'ground_price', 'ocean_price']].to_string(index=False))
import pandas as pd

from models import booking as b

def convert_to_dataframe(booking_obj : b.Booking) -> pd.DataFrame:
    d = {'air_price' : [booking_obj.route.air_price], 
         'ground_price' : [booking_obj.route.ground_price],
         'ocean_price' : [booking_obj.route.ocean_price],
         'preferred_route' : [booking_obj.route.preferred_route]}
    return pd.DataFrame(data=d)

def print_shipping_options(booking: pd.DataFrame):
    booking['air_price'] = booking['air_price'].replace([-1], '-') 
    booking['ground_price'] = booking['ground_price'].replace([-1], '-')    
    booking['ocean_price'] = booking['ocean_price'].replace([-1], '-')   
    print(booking[['air_price', 'ground_price', 'ocean_price', 'preferred_route']].to_string(index=False))
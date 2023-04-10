import pandas as pd

from models import booking as b
from utils import format as f

def convert_to_dataframe(booking_obj : b.Booking) -> pd.DataFrame:
    d = {'air_price' : [booking_obj.route.air_price], 
         'ground_price' : [booking_obj.route.ground_price],
         'ocean_price' : [booking_obj.route.ocean_price]}
    return pd.DataFrame(data=d)

def print_shipping_options(booking: pd.DataFrame):
    f.print_message("Available routing options")
    booking = booking.astype({'air_price':'string','ground_price':'string', 'ocean_price':'string'})
    booking['ground_price'] = '$' + booking['ground_price']
    booking['air_price'] = '$' + booking['air_price']
    booking['ocean_price'] = '$' + booking['ocean_price']
    booking['air_price'] = booking['air_price'].replace(['$-1.0'], '-') 
    booking['ground_price'] = booking['ground_price'].replace(['$-1.0'], '-')    
    booking['ocean_price'] = booking['ocean_price'].replace(['$-1.0'], '-')     
    print(booking[['air_price', 'ground_price', 'ocean_price']].to_string(index=False))
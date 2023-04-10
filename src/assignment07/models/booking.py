import pandas as pd

from models import route

class Booking:

    def __init__(self, booking_id = None, customer_name= None, destination_country= None, 
                 package_description= None, weight= None, volume= None, 
                 required_delivery_date= None, is_dangerous= False, is_urgent= False):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.destination_country = destination_country
        self.package_description = package_description
        self.weight = weight
        self.volume = volume
        self.required_delivery_date = required_delivery_date
        self.is_dangerous = is_dangerous
        self.is_urgent = is_urgent

    def set_route(self, route : route.Route) -> None:
        self.route = route

    def set_dataframe(self) -> pd.DataFrame:
        d = {'booking_id' : [self.booking_id],
            'customer_name' : [self.customer_name],
            'destination_country' : [self.destination_country],
            'package_description' : [self.package_description],
            'weight' : [self.weight],
            'volume' : [self.volume],         
            'required_delivery_date' : [self.required_delivery_date],
            'is_dangerous' : [self.is_dangerous],
            'is_urgent' : [self.is_urgent],
            'ground_price' : [self.route.ground_price],
            'air_price' : [self.route.air_price], 
            'ocean_price' : [self.route.ocean_price]
            }
        self.dataframe = pd.DataFrame(data=d)       
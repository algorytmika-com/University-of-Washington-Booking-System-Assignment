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

    def set_possible_delivery_date(self, possible_delivery_date):
        self.possible_delivery_date = possible_delivery_date

    def set_route(self, route : route.Route) -> None:
        self.route = route

       
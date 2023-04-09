class Booking:

    def __init__(self, booking_id, customer_name, destination_country, package_description, weight, volume, required_delivery_date, is_dangerous, is_urgent):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.destination_country = destination_country
        self.package_description = package_description
        self.weight = weight
        self.volume = volume
        self.required_delivery_date = required_delivery_date
        self.is_dangerous = is_dangerous
        self.is_urgent = is_urgent

    def set_price_accepted(self, price_accepted ):
        self.price_accepted = price_accepted         

    def set_route(self, route):
        self.route = route            
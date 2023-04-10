import sys, os

from controllers import file as f, booking as b
from utils import format as fmt
from models import booking

prompt = "\n".join(("Please choose from below options:",
          "1 - Add a new booking",
          "2 - Generate a report of all bookings",
          "3 - Generate a report of urgent booking",
          "4 - Generate a report of truck shipments",
          "5 - Generate a report of air shipments",
          "6 - Generate a report of ocean shipments",
          "7 - Generate a report of dangerous goods shipments",
          "8 - Quit",
          ">>> "))

def add_booking():
    while True:
        csv_path = f.get_path()
        bookings = f.get_dataframe_from_file(csv_path)
        booking_incremented_id = b.get_booking_max_id(bookings) + 1
        customer_name = b.get_input_customer_name()
        package_description = b.get_package_description()
        destination_country = b.get_destination_country()
        is_urgent = b.is_urgent()
        is_dangerous = b.is_dangerous()
        weight = b.get_input_weight()
        if weight == -1:
            break
        volume = b.get_input_volume()
        if volume == -1:
            break
        required_delivery_date = b.get_required_date()
        customer_booking = booking.Booking(booking_incremented_id, customer_name, destination_country, package_description, weight, volume, required_delivery_date, is_dangerous, is_urgent)
        print(booking_incremented_id, customer_name, destination_country, package_description, weight, volume, required_delivery_date, is_dangerous, is_urgent)
        route = b.get_route(customer_booking)
        customer_booking.set_route(route)
        print('is_ground=', route.is_ground)
        print('is_air=', route.is_air)
        print('is_ocean=', route.is_ocean)

        route = b.get_route_prices(customer_booking)
        print('ground_price=', route.ground_price)
        print('air_price=', route.air_price)
        print('ocean_price=', route.ocean_price)        
        break


def exit_program() -> None:
    print("Bye!")
    sys.exit() 

def clear_console() -> None:
    clear = lambda: os.system('cls')
    clear()

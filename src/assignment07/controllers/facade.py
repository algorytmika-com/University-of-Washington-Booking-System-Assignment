import sys, os

from controllers import file as f, booking as b, report as r
from models import booking

prompt = "\n".join(("Please choose from below options:",
          "1 - Add a new booking",
          "2 - Generate a report of all booking quotes",
          "3 - Generate a report of urgent booking quotes",
          "4 - Generate a report of dangerous goods shipments",
          "5 - Quit", 
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
        required_delivery_date = b.get_required_date(is_urgent)
        customer_booking = booking.Booking(booking_incremented_id, customer_name, destination_country, package_description, weight, volume, required_delivery_date, is_dangerous, is_urgent)
        route = b.get_route(customer_booking)
        customer_booking.set_route(route)
        route = b.get_route_prices(customer_booking)
        customer_booking.set_route(route)
        r.print_shipping_options(r.convert_to_dataframe(customer_booking), "AVAILABLE ROUTING OPTIONS")
        break

def report_all_bookings():
    csv_path = f.get_path()
    bookings = f.get_dataframe_from_file(csv_path)
    r.print_all_bookings(bookings, "ALL BOOKING QUOTES")

def report_urgent_bookings():
    csv_path = f.get_path()
    bookings = f.get_dataframe_from_file(csv_path)
    r.print_urgent_bookings(bookings, "URGENT BOOKING QUOTES")  

def report_dangerous_bookings():
    csv_path = f.get_path()
    bookings = f.get_dataframe_from_file(csv_path)
    r.print_dangerous_bookings(bookings, "BOOKING QUOTES WITH DANGEROUS PACKAGES")        

def exit_program() -> None:
    print("Bye!")
    sys.exit() 

def clear_console() -> None:
    clear = lambda: os.system('cls')
    clear()

import sys, os


from controllers import file as f, booking as b
from utils import format as fmt

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
        print(booking_incremented_id)
        consumer_name = b.get_input_consumer_name()
        print(consumer_name)
        package_description = b.get_package_description()
        print(package_description)
        is_dangerous = b.is_dangerous()
        print(is_dangerous)
        weight = b.get_input_weight()
        print(weight)
        if weight == -1:
            break
        volume = b.get_input_volume()
        print(volume)
        if volume == -1:
            break

        destination_country = b.get_destination_country()
        print(destination_country)
        break


def exit_program() -> None:
    print("Bye!")
    sys.exit() 

def clear_console() -> None:
    clear = lambda: os.system('cls')
    clear()

import sys, os


from controllers import file as f

prompt = "\n".join(("Please choose from below options:",
          "1 - Load bookings in from a file",
          "2 - Add a new booking",
          "3 - Generate a report of all bookings",
          "4 - Generate a report of urgent booking",
          "5 - Generate a report of truck shipments",
          "6 - Generate a report of air shipments",
          "7 - Generate a report of ocean shipments",
          "8 - Generate a report of dangerous goods shipments",
          "9 - Quit",
          ">>> "))

def get_bookings_from_file():
    global bookings
    csv_path = f.get_path()
    bookings = f.get_csv_content(csv_path)

def exit_program() -> None:
    print("Bye!")
    sys.exit() 

def clear_console() -> None:
    clear = lambda: os.system('cls')
    clear()
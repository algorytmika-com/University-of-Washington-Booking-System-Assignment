from controllers import facade as f
from utils import format as fmt


def main():
    while True:
        fmt.print_message("MENU")
        response = input(f.prompt)
        if response == "1":
            f.add_booking()
        elif response == "2":
            f.report_all_bookings()
        elif response == "3":
            f.report_urgent_bookings()
        elif response == "4":
            f.report_dangerous_bookings()
        elif response == "5":
            f.exit_program()
        else:
            print("Not a valid option!")


if __name__ == "__main__":
    main()

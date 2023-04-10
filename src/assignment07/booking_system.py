from controllers import facade as f
from utils import format as fmt

def main():
    while True:
        fmt.print_message("MENU")
        response = input(f.prompt)  
        f.clear_console()
        if response == "1":
            f.add_booking()
        elif response == "2":
            f.report_all_bookings()
        elif response == "3":
            pass
        elif response == "4":
            pass
        elif response == "5":
            pass  
        elif response == "6":        
            pass 
        elif response == "7":        
            pass       
        elif response == "8":
            f.exit_program()
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    main()
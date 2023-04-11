NEW_LINE_PROMPT = "\n>>>"
LOCATION_PROMPT = "Give the location and name of the database file that is relative " \
                  f"to the above path (e.g. /folder/hr.csv):{NEW_LINE_PROMPT}"


def print_message(message):
    length = len(message)
    if length < 50:
        message = 25 * ' ' + message + 25 * ' '
    separator = len(message) * '-'
    print('\n' + separator)
    print(message)
    print(separator + '\n')


def print_table(message):
    separator = 50 * '-'
    print('\n' + separator)
    print(message)
    print(separator + '\n')

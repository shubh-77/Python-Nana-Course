from helper import validate_and_execute, user_input_message
import logging

logger =logging.getLogger("MAIN")
logger.error("Error happened in the app")


days = ""
while days != 'exit':
    # Importing user input message
    days = input(user_input_message)
    days_and_units = days.split(":")
    # split will convert string to list
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    # module_name.meth_name()
    validate_and_execute(days_and_units_dictionary)

    # for day in set(list_of_days):
    #     #  set() will convert list to set.
    #     validate_and_execute()

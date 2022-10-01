def days_to_units(num_of_days, name_of_unit):
    if name_of_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} {name_of_unit}"
    elif name_of_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} {name_of_unit}"
    else:
        return "Unsupported unit"


def validate_and_execute(days_and_units_dictionary):
    #  to do conversion of positive integers only
    try:
        days_local = int(days_and_units_dictionary["days"])
        if days_local > 0:
            print(days_to_units(days_local, days_and_units_dictionary["units"]))
        elif days_local == 0:
            print("You entered 0,please enter a valid positive number")
        else:
            print("You entered -negative value ,no conversion")
    except ValueError:
        print("enter valid input to avoid program cash ")

user_input_message="Enter number of days & conversion unit eg. 45:hours\n"
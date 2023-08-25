"""This file converts lengths to mm and addresses maximum and minimum values."""

# functions go here

def convert_mm(input_length, input_unit):
    """Convert lengths to mm."""

    if input_unit == "m":
        converted = input_length * 1000
    elif input_unit == "cm":
        converted = input_length * 10
    elif input_unit == "mm":
        converted = input_length * 1
    else:
        print("Please enter a valid unit (mm, cm, m)")
        return None
    
    return converted


def get_valid_converted_length(min_value, max_value):
    """Get a valid converted length within the allowed range"""

    while True:
      try:
        entered_value = float(input("Enter your length: "))
        entered_unit = input("Enter the unit (mm, cm, m): ")
        converted_length = convert_mm(entered_value, entered_unit)

        if converted_length is not None and min_value <= converted_length <= max_value:
            return entered_value, entered_unit, converted_length
        else:
            print(f"Converted value should be between {min_value}mm and \
{max_value}mm. Try again.")
      except ValueError:
        print("Invalid input. Please enter a numerical value for length.")
        


# main routine goes here

def main():
    # set the allowed range
    minimum_allowed = 1  # 1mm
    maximum_allowed = 50000  # 50m in mm

    # get user input for the converted length
    entered_value, entered_unit, converted_length = get_valid_converted_length\
(minimum_allowed, maximum_allowed)

    print("Entered value:", entered_value, entered_unit)
    print("Converted length:", converted_length, "mm")


# Call the main function to run the program
main()

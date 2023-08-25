# functions go here

# checks that user enters a valid response
def string_checker(question, valid_responses):

  error = "Please choose from: {}".format(', '.join(valid_responses))

  while True:

    response = input(question).lower()

    for item in valid_responses:
      if response == item[0] or response == item:
        return item

    print(error)


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

# string checker variables
yes_no_list = ["yes", "no"]
shape_list = ["circle", "square", "triangle", "parallelogram"]

# set the allowed range for valid converted length
minimum_allowed = 1  # 1mm
maximum_allowed = 50000  # 50m in mm

# asks user if they want to read the instructions
want_instructions = string_checker("Do you want to read the instructions? (y/n): "\
                                     , yes_no_list)
if want_instructions == "yes":
  print("instructions go here")

print()

# asks the user to select a shape
select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram): ", shape_list)

print("You chose", select_shape)

# get user input for the converted length
entered_value, entered_unit, converted_length = get_valid_converted_length\
(minimum_allowed, maximum_allowed)

print("Entered value:", entered_value, entered_unit)
print("Converted length:", converted_length, "mm")
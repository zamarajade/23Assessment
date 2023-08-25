"""This file takes in values from the user, depending on shape they choose"""

# functions go here

# what shape based on a list of options
def string_checker(question, valid_responses):

  error = "Please choose from: {}".format(', '.join(valid_responses))

  while True:

    response = input(question).lower()

    for item in valid_responses:
      if response == item[0] or response == item:
        return item

    print(error)


def values(selected_shape):
  valid_units = ['mm', 'cm', 'm']
  
  while True:
      try:
          if selected_shape == "square" or selected_shape == "s":
              length = float(input("Please enter the length of your square: "))
              length_unit = input("Enter the unit (mm, cm, m): ")
              if length_unit not in valid_units:
                print("Invalid unit. Please choose from:", ', '.join(valid_units))
                continue
              print("Entered length:", length, length_unit)
              return length, length_unit
          elif selected_shape == "parallelogram" or selected_shape == "p":
              length = float(input("Please enter the length of your parallelogram: "))
              length_unit = input("Enter the unit (mm, cm, m): ")
              width = float(input("Please enter the width of your parallelogram: "))
              width_unit = input("Enter the unit (mm, cm, m): ")
              if length_unit not in valid_units or width_unit not in valid_units:
                print("Invalid unit. Please choose from:", ', '.join(valid_units))
                continue
              print("Entered length:", length, length_unit)
              print("Entered width:", width, width_unit)
              return length, length_unit, width, width_unit
          elif selected_shape == "triangle" or selected_shape == "t":
              length = float(input("Please enter the length of your triangle: "))
              length_unit = input("Enter the unit (mm, cm, m): ")
              angle = float(input("Please enter the angle of your triangle: "))
              height = float(input("Please enter the height of your triangle: "))
              height_unit = input("Enter the unit (mm, cm, m): ")
              if length_unit not in valid_units or height_unit not in valid_units:
                print("Invalid unit. Please choose from:", ', '.join(valid_units))
                continue
              print("Entered length:", length, length_unit)
              print("Entered angle:", angle, "degrees")
              print("Entered height:", height, height_unit)
              return length, length_unit, angle, height, height_unit
          elif selected_shape == "circle" or selected_shape == "c":
              radius = float(input("Please enter the radius of your circle: "))
              radius_unit = input("Enter the unit (mm, cm, m): ")
              diameter = float(input("Please enter the diameter of your circle: "))
              diameter_unit = input("Enter the unit (mm, cm, m): ")
              if radius_unit not in valid_units or diameter_unit not in valid_units:
                print("Invalid unit. Please choose from:", ', '.join(valid_units))
                continue
              print("Entered radius:", radius, radius_unit)
              print("Entered diameter", diameter, diameter_unit)
              return radius, radius_unit, diameter, diameter_unit
          else:
              print("error")
      except ValueError:
          print("Please enter a numerical value.")

      
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

shape_list = ["circle", "square", "triangle", "parallelogram"]

select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram):", shape_list)

print("You chose", select_shape)

# set the allowed range
minimum_allowed = 1  # 1mm
maximum_allowed = 50000  # 50m in mm

# convert each unit inputted by user
value_input = values(select_shape)

if select_shape == "circle":
    radius_input, radius_unit, diameter_input, diameter_unit = value_input
    converted_radius = convert_mm(radius_input, radius_unit)
    converted_diameter = convert_mm(diameter_input, diameter_unit)
    print("Converted radius:", converted_radius, "mm")
    print("Converted diameter:", converted_diameter, "mm")
elif select_shape == "square":
    length_input, length_unit = value_input
    converted_length = convert_mm(length_input, length_unit)
    print("Converted length:", converted_length, "mm")
elif select_shape == "parallelogram":
    length_input, length_unit, width_input, width_unit = value_input
    converted_length = convert_mm(length_input, length_unit)
    converted_width = convert_mm(width_input, width_unit)
    print("Converted length:", converted_length, "mm")
    print("Converted width:", converted_width, "mm")
elif select_shape == "triangle":
    length_input, length_unit, angle_input, height_input, height_unit = value_input
    converted_length = convert_mm(length_input, length_unit)
    converted_height = convert_mm(height_input, height_unit)
    print("Converted length:", converted_length, "mm")
    print("Converted height:", converted_height, "mm")
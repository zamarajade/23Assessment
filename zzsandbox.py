def values(selected_shape):
  valid_units = ['mm', 'cm', 'm']
  
  while True:
      try:
          if selected_shape == "square" or selected_shape == "s":
              length = float(input("Please enter the length of your square: "))
              while True:
                length_unit = input("Enter the unit (mm, cm, m): ")
                if length_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              print("Entered length:", length, length_unit)
              square_values.append(length)
              square_units.append(length_unit)            
              return length, length_unit
            
          elif selected_shape == "parallelogram" or selected_shape == "p":
              length = float(input("Please enter the length of your parallelogram: "))
              while True:
                length_unit = input("Enter the unit (mm, cm, m): ")
                if length_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              width = float(input("Please enter the width of your parallelogram: "))
              while True:
                width_unit = input("Enter the unit (mm, cm, m): ")
                if width_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              parallelogram_values.append(length)
              parallelogram_units.append(length_unit)
              parallelogram_values.append(width)
              parallelogram_units.append(width_unit)
              print("Entered length:", length, length_unit)
              print("Entered width:", width, width_unit)
              return length, length_unit, width, width_unit
            
          elif selected_shape == "triangle" or selected_shape == "t":
              length = float(input("Please enter the length of your triangle: "))
              while True:
                length_unit = input("Enter the unit (mm, cm, m): ")
                if length_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              angle = float(input("Please enter the angle of your triangle: "))
              height = float(input("Please enter the height of your triangle: "))
              while True:
                height_unit = input("Enter the unit (mm, cm, m): ")
                if height_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              triangle_values.append(length)
              triangle_units.append(length_unit)
              triangle_values.append(angle)
              triangle_units.append("degrees")
              triangle_values.append(height)
              triangle_units.append(height_unit)
              print("Entered length:", length, length_unit)
              print("Entered angle:", angle, "degrees")
              print("Entered height:", height, height_unit)
              return length, length_unit, angle, height, height_unit
            
          elif selected_shape == "circle" or selected_shape == "c":
              radius = float(input("Please enter the radius of your circle: "))
              while True:
                radius_unit = input("Enter the unit (mm, cm, m): ")
                if radius_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              diameter = float(input("Please enter the diameter of your circle: "))
              while True:
                diameter_unit = input("Enter the unit (mm, cm, m): ")
                if diameter_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              circle_values.append(radius)
              circle_units.append(radius_unit)
              circle_values.append(diameter)
              circle_units.append(diameter_unit)
              print("Entered radius:", radius, radius_unit)
              print("Entered diameter", diameter, diameter_unit)
              return radius, radius_unit, diameter, diameter_unit
          else:
              print("error")
      except ValueError:
          print("Please enter a numerical value.")


# what shape based on a list of options
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

#main

shape_list = ["circle", "square", "triangle", "parallelogram"]

# lists to hold shape details
square_values = []
square_units = []
circle_values = []
circle_units = []
triangle_values = []
triangle_units = []
parallelogram_values = []
parallelogram_units = []

select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram): ", shape_list).lower().strip()

print("You chose", select_shape)

entered_values = values(select_shape)

print()

if len(square_values) > 0:
    value1 = square_values[0]
    unit1 = square_units[0]
    converted_length = convert_mm(value1, unit1)
    print("Converted square length:", converted_length, "mm")

if len(circle_values) > 0:
    value1 = circle_values[0]
    unit1 = circle_units[0]
    converted_radius = convert_mm(value1, unit1)
    print("Converted circle radius:", converted_radius, "mm")
if len(circle_values) > 0:
  value2 = circle_values[1]
  unit2 = circle_units[1]
  converted_diameter = convert_mm(value2, unit2)
  print("Converted circle diameter:", converted_diameter, "mm")

if len(triangle_values) > 0:
  value1 = triangle_values[0]
  unit1 = triangle_units[0]
  converted_length = convert_mm(value1, unit1)
  print("Converted triangle length:", converted_length, "mm")
if len(triangle_values) > 0:
  value2 = triangle_values[1]
  unit2 = triangle_units[1]
  print("Triangle angle:", value2, unit2)
if len(triangle_values) > 0:
  value3 = triangle_values[2]
  unit3 = triangle_units[2]
  converted_height = convert_mm(value3, unit3)
  print("Converted triangle height:", converted_height, "mm")

if len(parallelogram_values) > 0:
  value1 = parallelogram_values[0]
  unit1 = parallelogram_units[0]
  converted_length = convert_mm(value1, unit1)
  print("Converted parallelogram length:", converted_length, "mm")
if len(parallelogram_values) > 0:
  value2 = parallelogram_values[1]
  unit2 = parallelogram_units[1]
  converted_width = convert_mm(value2, unit2)
  print("Converted parallelogram width:", converted_width, "mm")
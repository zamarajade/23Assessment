from datetime import date

import pandas as pd

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


# converts lengths to mm
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


# takes in values from user
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
              square_values.append(length)
              square_units.append(length_unit)
              print("Entered length:", length, length_unit)
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
              height = float(input("Please enter the perpendicular height of your \
parallelogram: "))
              while True:
                height_unit = input("Enter the unit (mm, cm, m): ")
                if height_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              parallelogram_values.append(length)
              parallelogram_units.append(length_unit)
              parallelogram_values.append(width)
              parallelogram_units.append(width_unit)
              parallelogram_values.append(height)
              parallelogram_units.append(height_unit)
              print("Entered length:", length, length_unit)
              print("Entered width:", width, width_unit)
              print("Entered height:", height, height_unit)
              return length, length_unit, width, width_unit, height, height_unit
            
          elif selected_shape == "triangle" or selected_shape == "t":
              base = float(input("Please enter the base length (side 1) of your \
triangle: "))
              while True:
                base_unit = input("Enter the unit (mm, cm, m): ")
                if base_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              side2 = float(input("Please enter the length of side 2 in your \
triangle: "))
              while True:
                side2_unit = input("Enter the unit (mm, cm, m): ")
                if side2_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              side3 = float(input("Please enter the length of side 3 in your \
triangle: "))
              while True:
                side3_unit = input("Enter the unit (mm, cm, m): ")
                if side3_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              height = float(input("Please enter the height of your triangle: "))
              while True:
                height_unit = input("Enter the unit (mm, cm, m): ")
                if height_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              angle = float(input("Please enter the angle of your triangle: "))
              triangle_values.append(base)
              triangle_units.append(base_unit)
              triangle_values.append(side2)
              triangle_units.append(side2_unit)
              triangle_values.append(side3)
              triangle_units.append(side3_unit)
              triangle_values.append(height)
              triangle_units.append(height_unit)
              triangle_values.append(angle)
              triangle_units.append("degrees")
              print("Entered base (side 1):", base, base_unit)
              print("Entered length of side 1:", side2, side2_unit)
              print("Entered length of side 2:", side3, side3_unit)
              print("Entered height:", height, height_unit)
              print("Entered angle:", angle, "degrees")
              return base, base_unit, side2, side2_unit, side3, side3_unit, height, \
            height_unit, angle 
            
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


# calculates area and perimeter based off of input
def equations():
    area_equation = None
    perimeter_equation = None

    if len(square_values) > 0:
        area_equation = converted_length ** 2
        perimeter_equation = converted_length * 4

    if len(circle_values) > 0:
        area_equation = pi * converted_radius ** 2
        perimeter_equation = 2 * pi * converted_radius

    if len(triangle_values) > 0:
        area_equation = 0.5 * converted_base * converted_height
        perimeter_equation = converted_base + converted_side2 + converted_side3

    if len(parallelogram_values) > 0:
        area_equation = converted_length * converted_height
        perimeter_equation = 2 * (converted_length + converted_width)

    return area_equation, perimeter_equation


# Function to collect values and units from user input
def get_values_and_units(shape_name, num_values):
    values = []
    units = []

    for i in range(num_values):
        value = float(input(f"Please enter the {shape_name} {i+1} value: "))
        unit = input("Enter the unit (mm, cm, m): ")
        converted_value = convert_mm(value, unit)

        values.append(converted_value)
        units.append(unit)

    return values, units


#main

shape_list = ["circle", "square", "triangle", "parallelogram", "xxx"]

# lists to hold shape details
square_values = []
square_units = []
circle_values = []
circle_units = []
triangle_values = []
triangle_units = []
parallelogram_values = []
parallelogram_units = []

# dictionaries to hold all shape details
all_shapes = []
all_lengths = []
all_widths = []
all_heights = []
all_radius = []
all_diameter = []
all_areas = []
all_perimeters = []

# Create a DataFrame from the dictionaries
area_perimeter_dict = {
    "Shape": all_shapes,
    "Length": all_lengths,
    "Width": all_widths,
    "Height": all_heights,
    "Radius": all_radius,
    "Diameter": all_diameter,
    "Area": all_areas,
    "Perimeter": all_perimeters
}
area_perimeter_frame = pd.DataFrame(area_perimeter_dict)

# shape dictionary
shapes = {
    "square": (square_values, square_units),
    "circle": (circle_values, circle_units),
    "triangle": (triangle_values, triangle_units),
    "parallelogram": (parallelogram_values, parallelogram_units)
}

# valid units
valid_units = ["mm", "cm", "m"]

# pi
pi = 3.141592

# set the allowed range
minimum_allowed = 1  # 1mm
maximum_allowed = 50000  # 50m in mm

# loop for shape calculations
while True:
  # asks user to select a shape
  select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram) or xxx to quit: ", shape_list).lower().strip()

  if select_shape == "xxx" and len(shapes) > 0:
   break
  elif select_shape == "xxx":
    print("You must make at least one calculation before quitting")
    continue

  print("You chose", select_shape)

  entered_values = values(select_shape)

  print()


  while True:
    select_shape = string_checker("Choose a shape (circle, square, triangle, parallelogram) or xxx to quit: ", shape_list).lower().strip()

    if select_shape == "xxx" and len(shapes) > 0:
        break
    elif select_shape == "xxx":
        print("You must make at least one calculation before quitting")
        continue

    print("You chose", select_shape)

    shape_values, shape_units = get_values_and_units(select_shape, len(shapes[select_shape]))

    shapes[select_shape] = (shape_values, shape_units)
    all_shapes.append(select_shape)

  
  
  # calculate area and perimeter
  area, perimeter = equations()
  if area is not None and perimeter is not None:
      print()
      print("Converted area: {:.2f}mm²".format(area))
      print("Converted perimeter: {:.2f}mm".format(perimeter))
      print()
      print()
      all_areas.append(area)
      all_perimeters.append(perimeter)

    

# Get current date for heading and filename
today = date.today()
day, month, year = today.strftime("%d"), today.strftime("%m"), today.strftime("%Y")

# Create formatted strings
heading = f"---- Area and Perimeter Calculation Data ({day}/{month}/{year}) ----\n"
information = "(all units are in mm)\n"
filename = f"MMF_{year}_{month}_{day}"

# Convert DataFrame to a formatted string
def format_length(length):
    if isinstance(length, tuple):
        return ", ".join(str(val) for val in length)
    return str(length)

area_perimeter_frame["Length"] = area_perimeter_frame["Length"].apply(format_length)
area_perimeter_string = area_perimeter_frame.to_string(index=False, float_format=\
                                                       "{:.2f}".format)

# List holding content to print / write to file
to_write = [heading, information, area_perimeter_string]

# Print output
for item in to_write:
    print(item)

# Write output to file
write_to = f"{filename}.txt"
with open(write_to, "w") as text_file:
    text_file.write("\n".join(to_write))
    
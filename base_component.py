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
                length_unit = input("Enter the unit (mm, cm, m): ").lower()
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
                length_unit = input("Enter the unit (mm, cm, m): ").lower()
                if length_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              width = float(input("Please enter the width of your parallelogram: "))
              while True:
                width_unit = input("Enter the unit (mm, cm, m): ").lower()
                if width_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              height = float(input("Please enter the perpendicular height of your \
parallelogram: "))
              while True:
                height_unit = input("Enter the unit (mm, cm, m): ").lower()
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
                base_unit = input("Enter the unit (mm, cm, m): ").lower()
                if base_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              side2 = float(input("Please enter the length of side 2 in your \
triangle: "))
              while True:
                side2_unit = input("Enter the unit (mm, cm, m): ").lower()
                if side2_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              side3 = float(input("Please enter the length of side 3 in your \
triangle: "))
              while True:
                side3_unit = input("Enter the unit (mm, cm, m): ").lower()
                if side3_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              height = float(input("Please enter the height of your triangle: "))
              while True:
                height_unit = input("Enter the unit (mm, cm, m): ").lower()
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
                radius_unit = input("Enter the unit (mm, cm, m): ").lower()
                if radius_unit not in valid_units:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))
                else:
                  break
              diameter = float(input("Please enter the diameter of your circle: "))
              while True:
                diameter_unit = input("Enter the unit (mm, cm, m): ").lower()
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


def show_instructions():
    print('''\n
***** Instructions *****

For each calculation, enter...
- What shape you have (can't be blank)
- The value of what the question asks you (between 1mm and 50m)
- The unit of the value you previously entered (mm, cm, m)
- Repeat for each question it asks for the shape you entered

When you have entered all the calculations, press 'xxx' to quit.

The program will then display the calculation details
including the area and perimeter for each shape.

All values entered will be converted into mm.

This information will also be automatically written
to a text file.

*************************''')


#main

yes_no_list = ["yes", "no"]
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


# ask user if they want instructions
want_instructions = string_checker("Do you want to read the instructions? (y/n): "\
                                     , yes_no_list)
print("You chose", want_instructions)
if want_instructions == "yes" or want_instructions == "y":
  instructions = show_instructions()
print()

# loop for shape calculations
while True:
  # reset the shape-specific lists at the start of each iteration
  square_values = []
  square_units = []
  circle_values = []
  circle_units = []
  triangle_values = []
  triangle_units = []
  parallelogram_values = []
  parallelogram_units = []

  # reset the variables - reduces errors
  converted_length = 0
  converted_width = 0
  converted_height = 0
  converted_radius = 0
  converted_diameter = 0
  converted_base = 0
  converted_side2 = 0
  converted_side3 = 0
  area = 0
  perimeter = 0

  # asks user to select a shape
  select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram) or xxx to quit: ", shape_list).lower().strip()

  if select_shape == "xxx" and len(all_shapes) > 0:
    break
  elif select_shape == "xxx":
    print("You must make at least one calculation before quitting")
    continue

  print("You chose", select_shape)

  entered_values = values(select_shape)

  print()


  # converts values from user input

  #converts square values from user input
  # converts sqaure length from user input
  if len(square_values) > 0:
      value1 = square_values[0]
      unit1 = square_units[0]

      while True:
          converted_length = convert_mm(value1, unit1)
          print("Converted square length:", converted_length, "mm")
   # checks to see if converted length is in valid range
          if converted_length is not None and minimum_allowed\
  <= converted_length <= maximum_allowed:
              break
          else:
   # asks user for new length if not in valid range          
              print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
              new_value = input("Enter a new length for your square: ")
              try:
                  value1 = float(new_value)
              except ValueError:
                  print("Please enter a numerical value.")
              new_unit = input("Enter a new unit for your length: ")
              if new_unit in valid_units:
                  unit1 = new_unit
                  converted_length = convert_mm(value1, unit1)
              else:
                  print("Invalid unit. Please choose from:", ', '.join(valid_units))


  # converts circle values from user input
  # converts circle radius from user input
  if len(circle_values) > 0:
    value1 = circle_values[0]
    unit1 = circle_units[0]
    while True:
      converted_radius = convert_mm(value1, unit1)
      print("Converted circle radius:", converted_radius, "mm")
  # checks to see if converted radius is in valid range
      if converted_radius is not None and minimum_allowed\
  <= converted_radius <= maximum_allowed:
        break
      else:
  # asks user for new radius if not in valid range
        print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
        new_value = input("Enter a new radius for your circle: ")
        try:
          value1 = float(new_value)
        except ValueError:
          print("Please enter a numerical value.") 
          
        new_unit = input("Enter a new unit for your radius: ")
        if new_unit in valid_units:
          unit1 = new_unit
          converted_radius = convert_mm(value1, unit1)
        else:
          print("Invalid unit. Please choose from:", ', '.join(valid_units))
    print()
  
  # converts circle diameter from user input
    if len(circle_values) > 0:
      value2 = circle_values[1]
      unit2 = circle_units[1]
      while True:
        converted_diameter = convert_mm(value2, unit2)
        print("Converted circle diameter:", converted_diameter, "mm")
  # checks to see if converted diameter is in valid range
        if converted_diameter is not None and minimum_allowed\
  <= converted_diameter <= maximum_allowed:
          break
        else:
  # asks user for new diameter if not in range
          print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
          new_value = input("Enter a new diameter for your circle: ")
          try:
            value2 = float(new_value)
          except ValueError:
            print("Please enter a numerical value.")
            
        new_unit = input("Please enter a new unit for your diameter: ")
        if new_unit in valid_units:
          unit2 = new_unit
          converted_diameter = convert_mm(value2, unit2)
        else:
          print("Invalid unit. Please choose from:", ', '.join(valid_units))
            
  
  # converts triangle values from user input
  # converts triangle base (side 1) from user input
  if len(triangle_values) > 0:
    value1 = triangle_values[0]
    unit1 = triangle_units[0]
    while True:
      converted_base = convert_mm(value1, unit1)
      print("Converted triangle base (side 1):", converted_base, "mm")
  # checks to see if converted base is in valid range
      if converted_base is not None and minimum_allowed <= converted_base\
  <= maximum_allowed:
        break
      else:
  # asks user for new base if not in range
        print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
        new_value = input("Enter a new base for your triangle: ")
        try:
          value1 = float(new_value)
        except ValueError:
          print("Please enter a numerical value.")
  
      new_unit = input("Please enter a new unit for your base: ")
      if new_unit in valid_units:
        unit1 = new_unit
        converted_base = convert_mm(value1, unit1)
      else:
        print("Invalid unit. Please choose from:", ', '.join(valid_units))
    print()
  
    # converts triangle side 2 length from user input
    if len(triangle_values) > 0:
      value2 = triangle_values[1]
      unit2 = triangle_units[1]
      while True:
        converted_side2 = convert_mm(value2, unit2)
        print("Converted triangle side 2 length:", converted_side2, "mm")
  # checks to see if converted side 2 length is in valid range
        if converted_side2 is not None and minimum_allowed <= converted_side2\
  <= maximum_allowed:
          break
        else:
  # asks user for new side 2 if not in range
          print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
          new_value = input("Enter a new side 2 length for your triangle: ")
          try:
            value2 = float(new_value)
          except ValueError:
            print("Please enter a numerical value.")
  
        new_unit = input("Please enter a new unit for your side 2 length: ")
        if new_unit in valid_units:
          unit2 = new_unit
          converted_side2 = convert_mm(value2, unit2)
        else:
          print("Invalid unit. Please choose from:", ', '.join(valid_units))
      print()
  
  # converts triangle side 3 length from user input
    if len(triangle_values) > 0:
      value3 = triangle_values[2]
      unit3 = triangle_units[2]
      while True:
        converted_side3 = convert_mm(value3, unit3)
        print("Converted triangle side 3 length:", converted_side3, "mm")
  # checks to see if converted side 3 length is in valid range
        if converted_side3 is not None and minimum_allowed <= converted_side3\
  <= maximum_allowed:
          break
        else:
  # asks user for new side 3 if not in range
          print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
          new_value = input("Enter a new side 3 length for your triangle: ")
          try:
            value3 = float(new_value)
          except ValueError:
            print("Please enter a numerical value.")
  
        new_unit = input("Please enter a new unit for your side 3 length: ")
        if new_unit in valid_units:
          unit3 = new_unit
          converted_side3 = convert_mm(value3, unit3)
        else:
          print("Invalid unit. Please choose from:", ', '.join(valid_units))
      print()
  
  # converts triangle height from user input
    if len(triangle_values) > 0:
      value4 = triangle_values[3]
      unit4 = triangle_units[3]
      while True:
        converted_height = convert_mm(value4, unit4)
        print("Converted triangle height:", converted_height, "mm")
  # checks to see if converted height is in valid range
        if converted_height is not None and minimum_allowed <= converted_height\
  <= maximum_allowed:
          break
        else:
  # asks user for new height if not in range
          print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
          new_value = input("Enter a new height for your triangle: ")
          try:
            value4 = float(new_value)
          except ValueError:
            print("Please enter a numerical value.")
  
        new_unit = input("Please enter a new unit for your height: ")
        if new_unit in valid_units:
          unit4 = new_unit
          converted_height = convert_mm(value4, unit4)
        else:
          print("Invalid unit. Please choose from:", ', '.join(valid_units))
      print()
  
  # checks to see if triangle angle is in valid range
    if len(triangle_values) > 0:
      value5 = triangle_values[4]
      unit5 = triangle_units[4]
      if value5 > 0 and value5 < 360:
        print("Triangle angle:", value5, unit5)
        print()
      else:
  # asks user for new angle if not in range
        print("Entered angle:", value5, unit5)
        print("Please enter an angle between 0 and 360")
        new_value = float(input("Please enter the angle for your triangle: "))
        if new_value > 0 and new_value < 360:
          try:
            value5 = new_value
          except ValueError:
             print("Please enter a numerical angle")
          print("Triangle angle:", value5, unit5)
          print()
  
  
  # converts parallelogram values from user input
  # converts parallelogram length from user input
  if len(parallelogram_values) > 0:
    value1 = parallelogram_values[0]
    unit1 = parallelogram_units[0]
    while True:
      converted_length = convert_mm(value1, unit1)
      print("Converted parallelogram length:", converted_length, "mm")
  # checks to see if converted length is in valid range
      if converted_length is not None and minimum_allowed <= converted_length\
  <= maximum_allowed:
        break
      else:
  # ask user for new length if not in range
        print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
        new_value = input("Enter a new length for your parallelogram: ")
        try:
          value1 = float(new_value)
        except ValueError:
          print("Please enter a numerical value.")
  
      new_unit = input("Please enter a new unit for your length: ")
      if new_unit in valid_units:
        unit1 = new_unit
        converted_length = convert_mm(value1, unit1)
      else:
        print("Invalid unit. Please choose from:",','.join(valid_units))
    print()
  
  # converts parallelogram width from user input
  if len(parallelogram_values) > 0:
    value2 = parallelogram_values[1]
    unit2 = parallelogram_units[1]
    while True:
      converted_width = convert_mm(value2, unit2)
      print("Converted parallelogram width:", converted_width, "mm")
  # checks to see if converted width is in valid range
      if converted_width is not None and minimum_allowed <= converted_width\
  <= maximum_allowed:
        break
      else:
  # ask user for new width if not in range
        print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
        new_value = input("Enter a new width for your parallelogram: ")
        try:
          value2 = float(new_value)
        except ValueError:
          print("Please enter a numerical value.")
  
      new_unit = input("Please enter a new unit for your width: ")
      if new_unit in valid_units:
        unit2 = new_unit
        converted_width = convert_mm(value2, unit2)
      else:
        print("Invalid unit. Please choose from:", ', '.join(valid_units))
    print()
  
  # converts parallelogram height from user input
  if len(parallelogram_values) > 0:
    value3 = parallelogram_values[2]
    unit3 = parallelogram_units[2]
    while True:
      converted_height = convert_mm(value3, unit3)
      print("Converted parallelogram height:", converted_height, "mm")
  # checks to see if converted height is in valid range
      if converted_height is not None and minimum_allowed <= converted_height \
  <= maximum_allowed:
        break
      else:
  # ask user for new height if not in range
        print(f"Converted value should be between {minimum_allowed}mm and \
  {maximum_allowed}mm. Try again.")
        new_value = input("Enter a new height for your parallelogram: ")
        try:
          value3 = float(new_value)
        except ValueError:
          print("Please enter a numerical value.")
  
      new_unit = input("Please enter a new unit for your height: ")
      if new_unit in valid_units:
        unit3 = new_unit
        converted_height = convert_mm(value3, unit3)
      else:
        print("Invalid unit. Please choose from:", ', '.join(valid_units))
    print()
  
  
  # calculate area and perimeter
  area, perimeter = equations()
  area = round(area, 2)
  perimeter = round(perimeter, 2)
    
  # Append values to the corresponding arrays
  if select_shape == "square":
      all_shapes.extend(["square", "-", "-"])
      all_lengths.extend([converted_length, "-", "-"])
      all_widths.extend(["-", "-", "-"])
      all_heights.extend(["-", "-", "-"])
      all_radius.extend(["-", "-", "-"])
      all_diameter.extend(["-", "-", "-"]) 
  elif select_shape == "circle":
      all_shapes.extend(["circle", "-", "-"])
      all_lengths.extend(["-", "-", "-"])
      all_widths.extend(["-", "-", "-"])
      all_heights.extend(["-", "-", "-"])
      all_radius.extend([converted_radius, "-", "-"])
      all_diameter.extend([converted_diameter, "-", "-"])
  elif select_shape == "triangle":
      all_shapes.extend(["triangle", "-", "-"])
      all_lengths.extend([converted_base, converted_side2, converted_side3])
      all_widths.extend(["-", "-", "-"]) 
      all_heights.extend([converted_height, "-", "-"]) 
      all_radius.extend(["-", "-", "-"]) 
      all_diameter.extend(["-", "-", "-"]) 
  elif select_shape == "parallelogram":
      all_shapes.extend(["parallelogram", "-", "-"])
      all_lengths.extend([converted_length, "-", "-"])
      all_widths.extend([converted_width, "-", "-"])
      all_heights.extend([converted_height, "-", "-"])
      all_radius.extend(["-", "-", "-"])  
      all_diameter.extend(["-", "-", "-"])
  else:
      # For shapes not selected, append zeros as placeholders
      all_shapes.extend(["-", "-", "-"])
      all_lengths.extend(["-", "-", "-"])
      all_widths.extend(["-", "-", "-"])
      all_heights.extend(["-", "-", "-"])
      all_radius.extend(["-", "-", "-"])
      all_diameter.extend(["-", "-", "-"])

  # Append area and perimeter to their respective lists
  all_areas.extend([area, "-", "-"])
  all_perimeters.extend([perimeter, "-", "-"])
  
  print()
  print()

    
# Create a DataFrame from the dictionaries
area_perimeter_dict = {
    "Shape": all_shapes,
    "Length(mm)": all_lengths,
    "Width(mm)": all_widths,
    "Height(mm)": all_heights,
    "Radius(mm)": all_radius,
    "Diameter(mm)": all_diameter,
    "Area(mm^2)": all_areas,
    "Perimeter(mm)": all_perimeters
}
area_perimeter_frame = pd.DataFrame(area_perimeter_dict)
area_perimeter_frame = area_perimeter_frame.round(2)


# Get current date for heading and filename
today = date.today()
day, month, year = today.strftime("%d"), today.strftime("%m"), today.strftime("%Y")

# Create formatted strings
heading = f"---- Area and Perimeter Calculation Data ({day}/{month}/{year}) ----\n"

filename = f"MMF_{year}_{month}_{day}"

# Convert DataFrame to a formatted string
def format_length(length):
    if isinstance(length, tuple):
        return ", ".join(str(val) for val in length)
    return str(length)


area_perimeter_string = area_perimeter_frame.to_string(index=False, float_format=\
                                                       "{:.1f}".format)

# List holding content to print / write to file
to_write = [heading, area_perimeter_string]

# Print output
print()
print()
for item in to_write:
    print(item)

# Write output to file
write_to = f"{filename}.txt"
with open(write_to, "w") as text_file:
    text_file.write("\n".join(to_write))
"""this test file is being used to test my valid range from conversion"""

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

# set the allowed range
minimum_allowed = 1  # 1mm
maximum_allowed = 50000  # 50m in mm

# valid units
valid_units = ["mm", "cm", "m"]

select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram): ", shape_list).lower().strip()

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
# converts triangle length from user input
if len(triangle_values) > 0:
  value1 = triangle_values[0]
  unit1 = triangle_units[0]
  while True:
    converted_length = convert_mm(value1, unit1)
    print("Converted triangle length:", converted_length, "mm")
# checks to see if converted length is in valid range
    if converted_length is not None and minimum_allowed <= converted_length\
<= maximum_allowed:
      break
    else:
# asks user for new length if not in range
      print(f"Converted value should be between {minimum_allowed}mm and \
{maximum_allowed}mm. Try again.")
      new_value = input("Enter a new length for your triangle: ")
      try:
        value1 = float(new_value)
      except ValueError:
        print("Please enter a numerical value.")

    new_unit = input("Please enter a new unit for your length: ")
    if new_unit in valid_units:
      unit1 = new_unit
      converted_length = convert_mm(value1, unit1)
    else:
      print("Invalid unit. Please choose from:", ', '.join(valid_units))
  print()

# checks to see if triangle angle is in valid range
  if len(triangle_values) > 0:
    value2 = triangle_values[1]
    unit2 = triangle_units[1]
    if value2 > 0 and value2 < 360:
      print("Triangle angle:", value2, unit2)
      print()
    else:
# asks user for new angle if not in range
      print("Entered angle:", value2, unit2)
      print("Please enter an angle between 0 and 360")
      new_value = float(input("Please enter the angle for your triangle: "))
      if new_value > 0 and new_value < 360:
        try:
          value2 = new_value
        except ValueError:
           print("Please enter a numerical angle")
        print("Triangle angle:", value2, unit2)
        print()

# converts triangle height from user input
  if len(triangle_values) > 0:
    value3 = triangle_values[2]
    unit3 = triangle_units[2]
    while True:
      converted_height = convert_mm(value3, unit3)
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

    new_unit = input("Please enter a new unit for your length: ")
    if new_unit in valid_units:
      unit2 = new_unit
      converted_width = convert_mm(value2, unit2)
    else:
      print("Invalid unit. Please choose from:",','.join(valid_units))
  print()
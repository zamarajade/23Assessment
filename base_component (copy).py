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

# list to hold all shape details
all_shapes = []
all_values = []
all_units = []
all_areas = []
all_perimeters = []

# dictionary used to create data frame
area_perimeter_dict = {
  "Shape": all_shapes,
  "Values": (all_values, all_units),
  "Areas": all_areas,
  "Perimeters": all_perimeters
}
# valid units
valid_units = ["mm", "cm", "m"]

# shape dictionary
shapes = {
    "square": (square_values, square_units),
    "circle": (circle_values, circle_units),
    "triangle": (triangle_values, triangle_units),
    "parallelogram": (parallelogram_values, parallelogram_units)
}

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
  if area is not None and perimeter is not None:
      print()
      print("Converted area: {:.2f}mm²".format(area))
      print("Converted perimeter: {:.2f}mm".format(perimeter))
    
   # Create a dictionary to store the current shape's information
      shape_info = {
          'shape': select_shape,
          'values': entered_values,
          'units': valid_units,
          'area': area,
          'perimeter': perimeter
    }

      # Append the dictionary to the respective lists
      all_shapes.append(shape_info['shape'])
      all_values.append((shape_info['values'], shape_info['units']))
      all_areas.append(shape_info['area'])
      all_perimeters.append(shape_info['perimeter'])
    
  else:
      print("No valid shape or values provided.")
    
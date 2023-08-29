"""This file takes in values from the user, depending on shape they choose"""

# functions go here

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



# main routine goes here

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

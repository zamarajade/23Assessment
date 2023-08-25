"""This file takes in values from the user, depending on shape they choose"""

# functions go here

# takes in values from user
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

select_shape = string_checker("Choose a shape (circle, square, triangle, \
parallelogram): ", shape_list).lower().strip()

print("You chose", select_shape)

entered_values = values(select_shape)
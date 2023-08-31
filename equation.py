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
        perimeter_equation = 2 * converted_length + converted_base

    if len(parallelogram_values) > 0:
        area_equation = converted_length * converted_height
        perimeter_equation = 2 * (converted_length + converted_width)

    return area_equation, perimeter_equation
    
# convert area and perimeter to original units
def convert_to_original_unit(value, original_unit, units_list):
    if original_unit == 'mm':
        return value, 'mm'
    elif original_unit == 'cm':
        return value / 10, 'cm'
    elif original_unit == 'm':
        return value / 1000, 'm'
    else:
        return None, None  


# main routine

square_values = [5]
square_units = ["m"]
circle_values = []
circle_units = []
triangle_values = []
triangle_units = []
parallelogram_values = []
parallelogram_units = []

# shape dictionary
shapes = {
    "square": (square_values, square_units),
    "circle": (circle_values, circle_units),
    "triangle": (triangle_values, triangle_units),
    "parallelogram": (parallelogram_values, parallelogram_units)
}

pi = 3.141592

converted_length = 5000

# calculate area and perimeter
area, perimeter = equations()
if area is not None and perimeter is not None:
    print()
    print(f"Converted area: {area}mm²")
    print(f"Converted perimeter: {perimeter}mm")
else:
    print("No valid shape or values provided.")

# convert area and perimeter back to unit inputted
select_shape = input("Enter the selected shape: ").lower()
if select_shape in shapes:
    values_list, units_list = shapes[select_shape]

    if area is not None and perimeter is not None:
        original_area, area_unit = convert_to_original_unit(area, units_list[0], \
units_list)
        original_perimeter, perimeter_unit = convert_to_original_unit(perimeter, \
units_list[0], units_list)

        if original_area is not None and original_perimeter is not None:
            print()
            print(f"Area: {original_area}{area_unit}²")
            print(f"Perimeter: {original_perimeter}{perimeter_unit}")
        else:
            print("Invalid original units.")
    else:
        print("No valid values provided.")
else:
    print("Invalid shape.")
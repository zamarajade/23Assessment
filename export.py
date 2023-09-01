import pandas as pd
from datetime import date

# functions go here

# dictionaries to hold all shape details
all_shapes = ["square", "circle", "triangle", "parallelogram"]
all_lengths = [7, 0, (3,4,5), 3] 
all_widths = [0, 0, 0, 2]
all_heights = [0, 0, 4, 4]
all_radius = [0, 3, 0, 0]
all_diameter = [0, 6, 0, 0]
all_areas = [49, 28.27, 6, 12]
all_perimeters = [28, 18.85, 12, 10]

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
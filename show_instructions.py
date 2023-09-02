# checks that user enters a valid response
def string_checker(question, valid_responses):

  error = "Please choose from: {}".format(', '.join(valid_responses))

  while True:

    response = input(question).lower()

    for item in valid_responses:
      if response == item[0] or response == item:
        return item

    print(error)

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

#variables

yes_no_list = ["yes", "no"]

#main

#ask user if they want to see instructions
want_instructions = string_checker("Do you want to read the instructions (y/n): ", \
                                   yes_no_list)

if want_instructions == "yes":
  show_instructions()

print()
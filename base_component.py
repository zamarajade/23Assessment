# functions go here

# checks if user says yes or no
def yes_no(question):

  while True:
    response = input(question).lower()
    if response == "yes" or response == "y":
      return "yes"
    elif response == "no" or response == "n":
      return "no"
    else:
      print("Please enter either yes or no.")

# asks user to select a shape
def shape_select(question):

  while True:
    response = input(question).lower().strip()
    if response == "circle" or response == "c":
      return "circle"
    elif response == "square" or response == "s":
      return "square"
    elif response == "triangle" or response == "t":
      return "triangle"
    elif response == "parallelogram" or response == "p":
      return "parallelogram"
    else:
      print("Please enter a valid shape")


# main routine goes here

want_instructions = yes_no("Do you need instructions for this program? Y/N ").lower()

if want_instructions == "yes":
  print("Instructions go here")
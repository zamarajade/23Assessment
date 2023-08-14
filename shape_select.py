# functions go here

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

while True:
  shape = shape_select("Choose a shape. (circle, square, triangle,\
 parallelogram): ").lower()

  print("You chose", shape)


  print()
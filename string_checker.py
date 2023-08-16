# checks that user enters a valid response
# what shape based on a list of options
def string_checker(question, valid_responses):

  error = "Please choose from: {}".format(', '.join(valid_responses))

  while True:

    response = input(question).lower()

    for item in valid_responses:
      if response == item[0] or response == item:
        return item

    print(error)


# main routine starts here

yes_no_list = ["yes", "no"]
shape_list = ["circle", "square", "triangle", "parallelogram"]


for _case in range(0, 5):
  want_instructions = string_checker("Do you want to read the instructions? (y/n): "\
                                     , yes_no_list)
  print("You chose", want_instructions)

print()

for _case in range(0, 10):
  select_shape = string_checker("Choose a shape (circle, square, triangle,\
  parallelogram): ", shape_list)

  print("You chose", select_shape)
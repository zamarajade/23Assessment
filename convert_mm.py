"""This file converts lengths to mm."""

# functions go here


def convert_mm(length):
  """Convert lengths to mm."""
  error = "Please enter a valid unit (mm, cm, m)"

  response = input("What unit?: ")

  if response == "m":
    converted = length*1000
    return converted

  elif response == "cm":
    converted = length*100
    return converted

  elif response == "mm":
    converted = length*1
    return converted

  else:
    print(error)
    return None


# main routine goes here

while True:
  try:
    length = float(input("Enter your length: "))
  except ValueError:
    print("Not a valid length")
    continue

  converted_length = convert_mm(length)

  if converted_length is not None:
    print("Converted length:", converted_length, "mm")
    break

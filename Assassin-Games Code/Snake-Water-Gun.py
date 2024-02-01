import random
import sys

# Displaying a welcome message
print("*** Welcome to the Snake-Water-Gun Game ***")
print("\n")


# Function to get human's choice
def human_choice():
  # Taking input from the user
  global uc1
  uc1 = int(
      input(
          "Enter your choice from '1' for Snake, '2' for Water and '3' for Gun : "
      ))

  # Defining global variables to store string representations of choices
  global s, w, g
  s = "Snake"
  w = "Water"
  g = "Gun"
  print("\n")

  # Displaying the user's choice based on input
  if uc1 == 1:
    print("Your Choice is : ", s)
  elif uc1 == 2:
    print("Your Choice is : ", w)
  elif uc1 == 3:
    print("Your Choice is : ", g)
  else:
    # Exit the program if the input is not 1, 2, or 3
    print("Invalid Input")
    sys.exit()

  print("\n")


# Function to get computer's choice
def comp_choice():
  # List of choices for the computer
  A = ["Snake", "Water", "Gun"]
  # Randomly selecting a choice for the computer
  global a1
  a1 = random.choice(A)
  print("Computer's Choice is : ", a1)


# Call functions to get choices
human_choice()
comp_choice()

print("\n")

# Checking the winner based on choices
if (uc1 == 1 and a1 == "Water") or (uc1 == 3
                                    and a1 == "Snake") or (uc1 == 2
                                                           and a1 == "Gun"):
  print("*** You Won ***")
elif (uc1 == 2 and a1 == "Snake") or (uc1 == 1
                                      and a1 == "Gun") or (uc1 == 3
                                                           and a1 == "Water"):
  print("*** Computer Won ***")
else:
  # If neither condition is met, it's a draw
  print("It's a Draw")

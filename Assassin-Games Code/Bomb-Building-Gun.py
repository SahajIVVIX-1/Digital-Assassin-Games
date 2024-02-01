import random
import sys

# Displaying a welcome message
print("*** Welcome to the Bomb-Building-Gun Game ***")
print("\n")


# Function to get human's choice
def human_choice():
  # Taking input from the user
  global uc3
  uc3 = int(
      input(
          "Enter your choice from '1' for Bomb, '2' for Building and '3' for Gun : "
      ))

  # Defining global variables to store string representations of choices
  global s, w, g
  s = "Bomb"
  w = "Building"
  g = "Gun"
  print("\n")

  # Displaying the user's choice based on input
  if uc3 == 1:
    print("Your Choice is : ", s)
  elif uc3 == 2:
    print("Your Choice is : ", w)
  elif uc3 == 3:
    print("Your Choice is : ", g)
  else:
    # Exit the program if the input is not 1, 2, or 3
    print("Invalid Input")
    sys.exit()

  print("\n")


# Function to get computer's choice
def comp_choice():
  # List of choices for the computer
  A = ["Bomb", "Building", "Gun"]
  # Randomly selecting a choice for the computer
  global a3
  a3 = random.choice(A)
  print("Computer's Choice is : ", a3)


# Call functions to get choices
human_choice()
comp_choice()

print("\n")

# Checking the winner based on choices
if (uc3 == 3 and a3 == "Bomb") or (uc3 == 2
                                   and a3 == "Gun") or (uc3 == 1
                                                        and a3 == "Building"):
  print("*** You Won ***")
elif (uc3 == 1 and a3 == "Gun") or (uc3 == 2 and a3 == "Bomb") or (
    uc3 == 3 and a3 == "Building"):
  print("*** Computer Won ***")
else:
  # If neither condition is met, it's a draw
  print("It's a Draw")

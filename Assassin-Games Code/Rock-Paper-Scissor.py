import random
import sys

# Displaying a welcome message
print("*** Welcome to the Rock-Paper-Scissor Game ***")
print("\n")


# Function to get human's choice
def human_choice():
  # Taking input from the user
  global uc2
  uc2 = int(
      input(
          "Enter your choice from '1' for Rock, '2' for Paper and '3' for Scissor : "
      ))

  # Defining global variables to store string representations of choices
  global s, w, g
  s = "Rock"
  w = "Paper"
  g = "Scissor"
  print("\n")

  # Displaying the user's choice based on input
  if uc2 == 1:
    print("Your Choice is : ", s)
  elif uc2 == 2:
    print("Your Choice is : ", w)
  elif uc2 == 3:
    print("Your Choice is : ", g)
  else:
    # Exit the program if the input is not 1, 2, or 3
    print("Invalid Input")
    sys.exit()

  print("\n")


# Function to get computer's choice
def comp_choice():
  # List of choices for the computer
  A = ["Rock", "Paper", "Scissor"]
  # Randomly selecting a choice for the computer
  global a2
  a2 = random.choice(A)
  print("Computer's Choice is : ", a2)


# Call functions to get choices
human_choice()
comp_choice()

print("\n")

# Checking the winner based on choices
if (uc2 == 1 and a2 == "Scissor") or (uc2 == 3
                                      and a2 == "Paper") or (uc2 == 2
                                                             and a2 == "Rock"):
  print("*** You Won ***")
elif (uc2 == 2 and a2 == "Scissor") or (uc2 == 1 and a2 == "Paper") or (
    uc2 == 3 and a2 == "Rock"):
  print("*** Computer Won ***")
else:
  # If neither condition is met, it's a draw
  print("It's a Draw")

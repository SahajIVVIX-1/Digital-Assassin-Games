import random
import sys


# Function for Snake-Water-Gun game
def Snake_Water_Gun():
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
      sys.exit(0)

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
  elif (uc1 == 2 and a1 == "Snake") or (uc1 == 1 and a1 == "Gun") or (
      uc1 == 3 and a1 == "Water"):
    print("*** Computer Won ***")
  else:
    # If neither condition is met, it's a draw
    print("It's a Draw")

  sys.exit(1)


# Function for Rock-Paper-Scissor game
def Rock_Paper_Scissor():
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
      sys.exit(0)

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
  if (uc2 == 1 and a2 == "Scissor") or (uc2 == 3 and a2 == "Paper") or (
      uc2 == 2 and a2 == "Rock"):
    print("*** You Won ***")
  elif (uc2 == 2 and a2 == "Scissor") or (uc2 == 1 and a2 == "Paper") or (
      uc2 == 3 and a2 == "Rock"):
    print("*** Computer Won ***")
  else:
    # If neither condition is met, it's a draw
    print("It's a Draw")
  sys.exit(1)


# Function for Bomb-Building-Gun game
def Bomb_Building_Gun():
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
      sys.exit(0)

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
  if (uc3 == 3 and a3 == "Bomb") or (uc3 == 2 and a3 == "Gun") or (
      uc3 == 1 and a3 == "Building"):
    print("*** You Won ***")
  elif (uc3 == 1 and a3 == "Gun") or (uc3 == 2 and a3 == "Bomb") or (
      uc3 == 3 and a3 == "Building"):
    print("*** Computer Won ***")
  else:
    # If neither condition is met, it's a draw
    print("It's a Draw")
  sys.exit(1)


# Main welcome message
print("*** Welcome to the Assassin Games ***")
print("\n")


# Function to get the user's choice
def user_main_choice():
  print("Enter 1 for Snake-Water-Gun")
  print("Enter 2 for Rock-Paper-Scissor")
  print("Enter 3 for Bomb-Building-Gun")
  print("\n")
  global uc0
  uc0 = int(input("Enter your choice : "))
  print("\n")

  if uc0 == 1:
    Snake_Water_Gun()
    sys.exit(2)
  elif uc0 == 2:
    Rock_Paper_Scissor()
    sys.exit(2)
  elif uc0 == 3:
    Bomb_Building_Gun()
    sys.exit(2)
  else:
    print("Invalid Input")
    sys.exit(0)


user_main_choice()

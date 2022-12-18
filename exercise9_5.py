# TASK: calculator application for three
# different volume calculations

# import functions from the file
from functions import *

while True:
    # ask user about the choice
    user_choice = input("Select the operation (1-3), 0 stops the applcation: \n")

    # if 0, stop the application
    if user_choice == "0":
        print("Thank you for using our application!")
        break

    # if 1, calculate box volume
    # by running the function
    elif user_choice == "1":
        width = float(input("Give box wigth:\n"))
        height = float(input("Give box height:\n"))
        depth = float(input("Give box depth:\n"))
        box_volume = box_volume(width, height, depth)
        print(f"Box volume: {box_volume} m3")
        print()

    # if 2, calculate ball volume
    # by running the function
    elif user_choice == "2":
        radius = float(input("Give ball radius:\n"))
        ball_volume = ball_volume(radius)
        print(f"Ball volume: {ball_volume} m3")
        print()

    # if 3, calculate pipe volume
    # by running the function
    elif user_choice == "3":
        radius = float(input("Give pipe radius:\n"))
        length = float(input("Give pipe length:\n"))
        pipe_volume = pipe_volume(radius, length)
        print(f"Pipe volume: {pipe_volume} m3")
        print()
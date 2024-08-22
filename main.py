import random
from turtle import Turtle, Screen
from tkinter import messagebox

def start_race():
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race. Choose a colour: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-100, -50, 0, 50, 100, 150]
    all_turtles = []


    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)
        
    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    messagebox.showinfo("You've won", f"The {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                    messagebox.showinfo("You've lost", f"The {winning_color} turtle is the winner!")
                play_again = messagebox.askyesno("Game Over", "Do you want to play again?")
                if play_again:
                    screen.clearscreen()
                    start_race()
                else:
                    screen.bye()
                break
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)

    screen.exitonclick()

start_race()

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def turn_left():
#     tim.left(10)

# def turn_right():
#     tim.right(10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(move_forwards, "w")  # Corrected order of arguments
# screen.onkey(move_backwards, "s")
# screen.onkey(turn_left, "a")
# screen.onkey(turn_right, "d")
# screen.onkey(clear, "c")


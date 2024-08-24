from turtle import Turtle, Screen
import tkinter as tk

tim = Turtle(shape="turtle")
tim.color("blue")
screen = Screen()
screen.title("Welcome to the turtle etch-a-sketch!")

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(move_forwards, "w")  # Corrected order of arguments
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.mainloop() 
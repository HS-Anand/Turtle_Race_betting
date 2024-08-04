from turtle import Turtle, Screen
import random
import turtle as tur

screen = Screen()
tur.title("Turtle Race Bet")

winner_turtle = "none"
race_is_on = False
screen.bgcolor("black")
speed = ["fastest", "fast", "normal", "slow", "slowest"]
colors = ["red", "yellow", "orange", "green", "blue", "purple"]

screen.setup(800,600)
bet_turtle = screen.textinput(title="Place you bet", prompt="Which turtle will win the race? Enter color:".lower())

turtles = []

timmy = Turtle()
timmy.penup()
timmy.goto(250, -300)
timmy.right(270)
timmy.pensize(15)
timmy.color("white")
timmy.pendown()
timmy.forward(600)
timmy.hideturtle()
t = Turtle()
t.penup()
t.goto(251, 300)
t.right(90)
t.pensize(4)
t.color("red")
t.pendown()
t.forward(600)
t.hideturtle()

pos1 = -250
pos2 = -125
for i in range(6):
    tim = Turtle()
    tim.shape("turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(pos1, pos2)
    pos2 = pos2 + 50
    turtles.append(tim)

if bet_turtle:
    race_is_on = True

while race_is_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winner_turtle = turtle.pencolor()
        turtle.forward(random.randint(1, 10))






timmy.penup()
timmy.goto(0,265)
timmy.hideturtle()
timmy.pencolor("green")
timmy.pendown()
timmy.write(f"Winner: {winner_turtle}", False, "center", ("Verdana",
                                    25, "normal"))
final = ["Won", "Lost"]
t.penup()
t.goto(0, 235)
t.hideturtle()
t.pencolor("green")
t.pendown()
f = 1
if winner_turtle == bet_turtle:
    f = 0
t.write(f"You {final[f]}!!", False, "center", ("Verdana",
                                        15, "normal"))




screen.exitonclick()

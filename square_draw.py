import turtle
import math

#Initialization
screen=turtle.Screen()
screen.bgcolor("black")
initial=turtle.Turtle()
initial.shape("turtle")
initial.color("white")
initial.penup()
initial.setx(0)
initial.sety(0)
initial.pendown()    

def square_spiral():
    global initial
    length = 4
    displacement = -.4
    drawSpeed = 10000
    setAngle = 90
    #Initial Outline
    for i in range(0,4):
         initial.forward(length)
         initial.right(setAngle)
         initial.speed(drawSpeed)         
    #Spiral In
    for i in range(1,1000):
        distance = math.sqrt((length * length) + (displacement * displacement))
        turnAngle = math.atan(displacement/length)
        turnAngle = math.degrees(turnAngle)
        initial.forward(distance)
        initial.right(setAngle+turnAngle)
        initial.speed(drawSpeed)
        length = length - displacement
    screen.exitonclick()

def start():
    square_spiral()

start()
    

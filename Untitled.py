import turtle
import serial
turtle = turtle.Turtle()
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
size = 200
turtle.speed(0)
turtle.pensize(5)

def drawPoints(dist1, dist2, pos):
    turtle.goto(0,0)
    turtle.setheading(pos)
    turtle.penup()
    turtle.forward(dist1 -1)
    turtle.pendown()
    turtle.forward(1)
    turtle.penup()
    turtle.backward((dist1 + dist2) - 1)
    turtle.pendown()
    turtle.backward(1)
    turtle.penup()
    turtle.forward(dist2)

def resetBackgroud(pos):
    if pos <= 1:
        turtle.clear()
        drawBackground()
    if pos >= 179:
        turtle.clear()
        drawBackground()

def readLine(line):
    data = line.decode("utf-8")
    sizeRatio = size/100
    try:
        dist1, dist2, pos = data.split()
    except:
        return 0
    return [int(dist1)*sizeRatio, int(dist2)*sizeRatio, int(pos)]

def drawBackground():
    turtle.goto(0,0)
    turtle.penup()
    turtle.sety(turtle.ycor() - size)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.sety(turtle.ycor() + size)
    
drawBackground()
turtle.pencolor("#00FF00")

while True:
    data = ser.readline()
    try:
        dist1, dist2, pos = readLine(data)
    except: continue
    resetBackgroud(pos)
    drawPoints(dist1, dist2, pos)

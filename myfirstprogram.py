from turtle import *
speed(0)
bgcolor('black')
color('green')
for i in range (160):
    rt(i)
    circle(150,i)
    fd(i)
    rt(90)
hideturtle()    
done()
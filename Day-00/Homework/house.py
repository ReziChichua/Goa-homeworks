from turtle import *


speed(5)
width(7)
 
color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#square done

#door

forward(70)
begin_fill()
color("pink")
left(90)

forward(120) #height of door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(50,70)
pendown()
begin_fill()
right(150)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
left(90)
forward(40)
end_fill()

penup()
goto(150,70)
pendown()
begin_fill()
forward(40)
left(90)
forward(60)
left(90)
forward(40)
left(90)
forward(60)
end_fill()


exitonclick()
import turtle
from random import randint
import Geometry_game
import sys

# total arguments
argNum = (len(sys.argv))-1


# Create rectangle object
rectangle= Geometry_game.GraphicRectangle(Geometry_game.Point(randint(0, 200), randint(0, 200)),
                                   Geometry_game.Point(randint(201, 400), randint(201, 400)))

# print rectangle coordinates
print("rectangle coordinates : ",
      rectangle.pointl.x,",",
      rectangle.pointl.y," and ",
      rectangle.pointh.x,",",
      rectangle.pointh.y)

myturtle= turtle.Turtle()

rectangle.draw(myturtle)


if argNum == 2 :
    # get point from user
    #user_point = Geometry_game.GraphicPoint(float(input("Guess X : ")),float(input("Guess Y : ")))
    user_point = Geometry_game.GraphicPoint(float(sys.argv[1]), float(sys.argv[2]))

    # print the game result
    if user_point.falls_in_rectangle(rectangle):
        print("Your point is inside the rectangle")
    else:
        print("Your point is outside the rectangle")

    user_point.draw(myturtle)


print("Area of rectangle : ", rectangle.area())

turtle.done()

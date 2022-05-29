import turtle

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (rectangle.pointl.x < self.x < rectangle.pointh.x) and \
                (rectangle.pointl.y < self.y < rectangle.pointh.y):
            return True
        else:
            return False

class GraphicPoint(Point):

    def draw(self,canvas,size=5, color='red'):

        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size,color)


class Rectangle:

    def __init__(self,pointl, pointh):
        self.pointl = pointl
        self.pointh = pointh

    def  area(self):
        return (self.pointh.x - self.pointl.x)* \
               (self.pointh.y - self.pointl.y)


class GraphicRectangle(Rectangle):

    def draw(self,canvas):

        canvas.penup()
        canvas.goto(self.pointl.x,self.pointl.y)

        canvas.pendown()
        canvas.forward(self.pointh.x - self.pointl.x)
        canvas.left(90)
        canvas.forward(self.pointh.y - self.pointl.y)
        canvas.left(90)
        canvas.forward(self.pointh.x - self.pointl.x)
        canvas.left(90)
        canvas.forward(self.pointh.y - self.pointl.y)
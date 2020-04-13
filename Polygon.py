__author__='Amit Verma'
import turtle

class Polygon:
	'''Base class for polygon'''
	def __init__(self,name,sides,color='black',line_thickness=5,length=100):
		self.name=name
		self.sides=sides
		self.color=color
		self.length=length
		
		self.line_thickness=line_thickness
		self.total_angle=(self.sides-2)*180
		self.each_angle=self.total_angle/self.sides
		
	def draw(self):
		win=turtle.Screen()
		win.title('Polygon')
		
		t=turtle.Turtle()
		t.color(self.color)
		t.pensize(self.line_thickness)
		t.begin_fill()
		for i in range(self.sides):
			t.forward(self.length)
			t.left(180-self.each_angle)
		t.end_fill()
		t.up()
		t.color('black')
		t.right(90)
		t.forward(100)
		t.down()
		t.write(self.name)
		
		turtle.exitonclick()
		
		

class Triangle(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Triangle',3,color,line_thickness,length)	
		

class Square(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Square',4,color,line_thickness,length)


class Rectangle(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
	
		
		super().__init__('Rectangle',4,color,line_thickness,length)	
		
class Pentagon(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Pentagon',5,color,line_thickness,length)
		
class Hexagon(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Hexagon',6,color,line_thickness,length)
		
class Heptagon(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Heptagon',7,color,line_thickness,length)
		
class Octaon(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Octagon',8,color,line_thickness,length)

class Nonagon(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Nonagon',9,color,line_thickness,length)		

class Decagon(Polygon):
	def __init__(self,color='black',line_thickness=5,length=100):
		super().__init__('Decagon',10,color,line_thickness,length)	


p1=Triangle(color='red')
p1.draw()

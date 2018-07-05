import turtle, math, time, pyautogui

turtle.bgcolor('red')
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("black")
myPen.pensize(1)
side=300
myPen.penup()
myPen.goto(0,0) 
myPen.pendown()

inc = 7
pi = math.pi
angle = 0
pyautogui.hotkey('alt', 'space')
pyautogui.press('x')
for i in range (0,1000):
	if i % 4 == 0  and i != 0:
		angle = math.tan(inc/side)
		temp = inc/(math.sin(angle))
		angle = 360*angle/(2*pi)
		myPen.left(90+angle)
		myPen.forward(temp)
		side = (side-inc)*(side-inc)+(inc*inc)
		side = math.sqrt(side)
	else:
		myPen.left(90)
		myPen.forward(side)
	if side < 10:
		break


inc = 7
pi = math.pi
angle = 0
side = 300
myPen1 = turtle.Turtle()
myPen1.goto(-300,0) 
myPen1.pendown()
myPen1.speed(0)
myPen1.color("black")
myPen1.pensize(1)
myPen1.right(90)
time.sleep(1)
for i in range (0,1000):
	if i % 4 == 0  and i != 0:
		angle = math.tan(inc/side)
		temp = inc/(math.sin(angle))
		angle = 360*angle/(2*pi)
		myPen1.right(90+angle)
		myPen1.forward(temp)
		side = (side-inc)*(side-inc)+(inc*inc)
		side = math.sqrt(side)
	else:
		myPen1.right(90)
		myPen1.forward(side)
	if side < 10:
		break


inc = 7
pi = math.pi
angle = 0
side = 300
myPen2 = turtle.Turtle()
myPen2.goto(0,0) 
myPen2.pendown()
myPen2.speed(0)
myPen2.color("black")
myPen2.pensize(1)
#myPen2.right(90)
time.sleep(1)
for i in range (0,1000):
	if i % 4 == 0  and i != 0:
		angle = math.tan(inc/side)
		temp = inc/(math.sin(angle))
		angle = 360*angle/(2*pi)
		myPen2.right(90+angle)
		myPen2.forward(temp)
		side = (side-inc)*(side-inc)+(inc*inc)
		side = math.sqrt(side)
	else:
		myPen2.right(90)
		myPen2.forward(side)
	if side < 10:
		break
		
inc = 7
pi = math.pi
angle = 0
side = 300
myPen3 = turtle.Turtle()
myPen3.goto(-300,0) 
myPen3.pendown()
myPen3.speed(0)
myPen3.color("black")
myPen3.pensize(1)
myPen3.left(90)
time.sleep(1)
for i in range (0,1000):
	if i % 4 == 0  and i != 0:
		angle = math.tan(inc/side)
		temp = inc/(math.sin(angle))
		angle = 360*angle/(2*pi)
		myPen3.left(90+angle)
		myPen3.forward(temp)
		side = (side-inc)*(side-inc)+(inc*inc)
		side = math.sqrt(side)
	else:
		myPen3.left(90)
		myPen3.forward(side)
	if side < 10:
		break



import turtle as tu

roo=tu.Turtle()
wn=tu.Screen()
wn.bgcolor('black')
wn.title('trying to impress my friends')
roo.left(90)
roo.speed(20)



def draw(l):
    if(l<10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("cyan")
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)

roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("yellow")
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)

roo.left(270)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("magenta")
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)
roo.right(90)
roo.speed(2000)

def draw(l):
    if(l<10):
        return
    else:

        roo.pensize(2)
        roo.pencolor("#FFF8DC")
        roo.forward(l)
        roo.left(30)
        draw(6*l/7)
        roo.left(30)
        roo.pensize(2)
        roo.backward(l)

draw(60)

wn.exitonclick()
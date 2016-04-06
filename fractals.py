#Draw a Sierpinski Triangle with turtle


import turtle

window = turtle.Screen()
nate = turtle.Turtle()
nate.shape('turtle')
nate.color('#669900')
nate.fillcolor('#669900')

def draw_sierpinski(length,depth):
    if depth==0:
        nate.begin_fill()
        for i in range(0,3):
            nate.fd(length)
            nate.left(120)
        nate.end_fill()
            
    else:
        draw_sierpinski(length/2,depth-1)
        nate.fd(length/2)
        draw_sierpinski(length/2,depth-1)
        nate.bk(length/2)
        nate.left(60)
        nate.fd(length/2)
        nate.right(60)
        draw_sierpinski(length/2,depth-1)
        nate.left(60)
        nate.bk(length/2)
        nate.right(60)

draw_sierpinski(200,3)

window.exitonclick()

import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Turtle Python")

turtle_instance = turtle.Turtle()
turtle_instance.color("blue")

def shrinkingSquare(size):
    for move in range(4):
        turtle_instance.forward(size)
        turtle_instance.left(90)
        size = size - 5
shrinkingSquare(150)
shrinkingSquare(130)
shrinkingSquare(110)
shrinkingSquare(90)
shrinkingSquare(70)
shrinkingSquare(50)
shrinkingSquare(30)

turtle.done()


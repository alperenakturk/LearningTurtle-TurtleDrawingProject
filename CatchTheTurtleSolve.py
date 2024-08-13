import turtle
import random

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ('Arial', 30, 'normal')
'''Yazılım jargonunda büyük harfle böyle değişken yazmak onun sabit olduğunu ve başka
yerlerde kullanılabileceğini gösteriyor bize.'''
score = 0
game_over = False # oyun bittiğinde true olacak ve her şey duracak

#turtle list
turtle_list = []

#score turtle
score_turtle = turtle.Turtle()

#countdown turtle
countdown_turtle = turtle.Turtle()

#make_turtle properties
x_coordinates = [-20, -10, 0, 10, 20]
y_coordinates = [-20, -10, 0, 10, 20]
grid_size = 10

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.color("dark blue")

    top_height = screen.window_height() / 2
    y = top_height * 0.9

    score_turtle.setpos(0,y)
    score_turtle.write(arg="Score: 0",move=False, align="center", font=(FONT))

def make_turtle(x, y):
    t = turtle.Turtle()

    def handle_click(x,y):
        '''Sadece tıklamayı ölçüyor da olsam on click fonksiyonu ile
        çağırdığım için x,y şeklinde koordinatlara ihtiyacım var.'''
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=(FONT))

    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    t.color("dark green")
    t.goto(x * grid_size, y * grid_size)
    turtle_list.append(t) #Oluşan tüm turtleları oluşturduğumuz listeye koyduk.


def setup_turtles():
    for x in x_coordinates:
        for y in y_coordinates:
            make_turtle(x, y)

def hide_turtles():
    for t in turtle_list:
        t.hideturtle()


#recursive function -->
def show_turtles_randomly():
    if not game_over: #Game over false ise çalış
        hide_turtles()
        random.choice(turtle_list).showturtle() #turtle listten random bir elemanı seç ve göster
        screen.ontimer(show_turtles_randomly,1000)

def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    countdown_turtle.color("dark blue")
    top_height = screen.window_height() / 2
    y = top_height * 0.85
    countdown_turtle.setpos(0,y-30)
    countdown_turtle.clear()

    if time > 0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Time:{time}",move=False, align="center", font=(FONT))
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        countdown_turtle.clear()
        hide_turtles()
        countdown_turtle.write(arg="Game Over!",move=False, align="center", font=(FONT))


def start_game_up():
    turtle.tracer(0) #Gelecek animasyonları sıfırlar ve arka planda gerçekleştirir.
    setup_score_turtle()
    setup_turtles()
    hide_turtles()
    show_turtles_randomly()
    countdown(10)
    turtle.tracer(1) #Animasyonların sonunu.Bu sayede setup animasyonlarının oluşumunu atlarım.

start_game_up()

turtle.mainloop()

import turtle
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("black") #Tahtanın rengi
turtle_screen.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle.speed(0) #imleçin hızı (0 en hızlısı)
turtle_instance.color("blue")
turtle_colors = ["red", "purple", "blue", "green", "orange", "yellow"]

for i in range(12):
    turtle_instance.color(turtle_colors[i%6])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)

turtle.mainloop()
'''
turtle.done ın aksine daha komplike işlemler için kullanılır.Uygulama 
bittikten sonra da kullanıcıdan input almaya devam eder.
'''

#turtle.done()
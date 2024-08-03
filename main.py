import turtle

drawing_board = turtle.Screen() #Tahta oluşturur
drawing_board.bgcolor("Light blue") #Tahta rengi
drawing_board.title("Python Turtle") #Uygulama başlığı


''' DENEME KODLARI
turtle_instance = turtle.Turtle()
turtle_instance.forward(100)
turtle_instance_2 = turtle.Turtle()
turtle_instance_2.left(45)
turtle_instance_2.forward(100)
'''


''' SQUARE
turtle_instance = turtle.Turtle()
for forward in range(4):
    turtle_instance.forward(100)
    turtle_instance.left(90)
'''

'''STAR
turtle_instance = turtle.Turtle()
for move in range(6):
    turtle_instance.right(144)
    turtle_instance.forward(100)
'''

#''' POLYGON
turtle_instance = turtle.Turtle() #Hareket edecek imleci oluşturma
num_sides = 6
angle = 360.0 / num_sides
side_length = 100.0

for move in range(num_sides):
    turtle_instance.right(angle) #sağ tarafa doğru x derece dön
    turtle_instance.forward(side_length) #ilerle
#'''

turtle.done() #Uygulamayı direkt kapatmak yerine bittiği zaman durdur.
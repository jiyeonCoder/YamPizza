#Yam Pizza Ver.1.0
#Written by Jiyeon Choi
#Jun.17.2021.

import turtle as t
import random
from playsound import playsound

#Set score as 0
score = 0
# Check if the game is currently playing
playing = False
#Background music
playsound('yamPizza_music.wav', block=False)


#Turn turtle right
def turn_right():
    t.setheading(0)


#Turn turtle upward
def turn_up():
    t.setheading(90)


#Turn turtle left
def turn_left():
    t.setheading(180)


#Turn turtle downward
def turn_down():
    t.setheading(270)


#Start the game after pressing the Spacebar
def start():
    global playing
    playing = True
    t.clear()
    play()


#Play the game
def play():
    global score
    global playing
    t.forward(10)

    # 25% chance the enemy towards to you
    if random.randint(1, 4) == 1:
        ang = te.towards(t.pos())
        te.setheading(ang)
    speed = score + 5

    # Enemy turtle's speed limit 20
    if speed > 20:
        speed = 20
    te.forward(speed)

    # Game over if you are too close from the enemy turtle
    if t.distance(te) < 10:
        text = "Score: " + str(score)
        message("Game Over", text)
        playing = False
        score = 0

    # Get 1 score if you eat the pizza
    if t.distance(tf) < 18:
        score = score + 1
        t.write(score)
        #relocate the pizza in random places
        star_x = random.randint(-250, -250)
        star_y = random.randint(-250, 250)
        tf.goto(star_x, star_y)

    #Play the game every 100 milliseconds(=0.1 sec).
    if playing:
        t.ontimer(play, 100)


#Show the messages on the start window.
def message(m1, m2):
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 30))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 15))
    t.home()


#Set Window's title, size and background.
t.title("Yam Pizza")
t.setup(600, 600)
t.bgcolor("purple")

#Create an enemy turtle and locate it on the upper part of the window.
te = t.Turtle()
te.shape("turtle")
te.color("red")
te.speed(0) #speed(0) is the max.
te.up()
te.goto(0, 200)

#Load the pizza image and add it to screen object.
pizzaImg = "pizza.gif"
screen = t.Screen()
screen.addshape(pizzaImg)

#Create the pizza and locate it on the lower part of the window.
tf = t.Turtle()
tf.shape(pizzaImg)
tf.up()
tf.speed(0)
tf.goto(0, -200)

#Create a turtle that you can control.
t.shape("turtle")
t.speed(0)
t.up()
t.color("orange")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Yam Pizza", "Press the [Spacebar] to Start")

t.mainloop()
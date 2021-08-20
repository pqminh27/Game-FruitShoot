import pgzrun
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'blue')
    screen.fill("cyan")
    # color background
    apple.draw()
    pineapple.draw()
    orange.draw()

def place_apple():
    apple.x = randint(0, 750)
    apple.y = randint(0, 550)

def place_pineapple():
    pineapple.x = randint(40, 700)
    pineapple.y = randint(40, 500)
place_pineapple()

def place_orange():
    orange.x = randint(40, 600)
    orange.y = randint(40, 300)
place_orange()

def on_mouse_down(pos):
        if apple.collidepoint(pos):
            print("Good shot!!!")
            place_apple()
        else:
            print("Missed the Apple!!!")
        if pineapple.collidepoint(pos):
            place_pineapple() 
        if orange.collidepoint(pos):
            place_orange()
    
pgzrun.go()

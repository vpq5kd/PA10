# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import uvage
import random
camera = uvage.Camera(800,600)
def lines():

    for i in range(0,800,100):
        randomx = random.randint(100, 700)
        line1 = uvage.from_color((randomx / 2), i, 'red', randomx, 40)
        line2randomx = 840 - randomx
        line2 = uvage.from_color(875 - (line2randomx / 2), i, 'red', 785 - randomx, 40)
        camera.draw(line1)
        camera.draw(line2)

lines()



def tick():
    if uvage.is_pressing('w') :
        camera.move(0,100)
    camera.display() # you almost always want to end this method with this line
# tell uvage to call the tick method 30 times per second
uvage.timer_loop(30, tick)
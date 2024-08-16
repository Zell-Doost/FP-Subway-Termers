import math
from pynput import keyboard
from pynput.keyboard import Key

W, S, A, D, Q, E = 1, 2, 3, 4, 5, 6


def input_to_string(n):
    return str(n.char)

class Player:
    def __init__(self, position):
        self.position = position
        self.angle = 0
        self.health = 100
        self.speed = 1
        self.inputs = []

    def input_handle(self, inputs):
        self.inputs = inputs

    def move(self):

        if self.inputs[W] == True:
        #if self.inputs:
            #return type(self.inputs[0])
            self.position[0] += self.speed*math.cos(self.angle)
            self.position[1] -= self.speed*math.sin(self.angle)

        if self.inputs[S] == True:
            self.position[0] -= self.speed*math.cos(self.angle)
            self.position[1] += self.speed*math.sin(self.angle)

        if self.inputs[A] == True:
            self.position[0] -= self.speed*math.sin(self.angle)

            self.position[1] -= self.speed*math.cos(self.angle)

        if self.inputs[D] == True:
            self.position[0] += self.speed*math.sin(self.angle)

            self.position[1] += self.speed*math.cos(self.angle)
        
        if self.inputs[Q] == True:
            self.angle += 0.1

        if self.inputs[E] == True:
            self.angle -= 0.1


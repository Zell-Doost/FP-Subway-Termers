import math
from pynput import keyboard
from pynput.keyboard import Key

W, S, A, D, Q, E = 1, 2, 3, 4, 5, 6


def input_to_string(n):
    return str(n.char)

class Player:
    def __init__(self):
        self.x = 21
        self.y = 3
        self.angle = math.pi
        self.sliding = False
        self.slide_timer = 0
        self.jumping = False
        self.jumping_timer = 0

    def move(self, inputs, timer):
        
        self.x -= 0.1
        

        if inputs[W] == True:
            if self.jumping_timer == 0:
                self.jumping = True
                self.jump_timer = timer
        if self.jumping and timer - self.jump_timer > 20:
            inputs[W] = False
            self.jump_timer = 0
            self.jumping = False

        if inputs[S] == True:
            if self.slide_timer == 0:
                self.sliding = True
                self.slide_timer = timer
        if self.sliding and timer - self.slide_timer > 20:
            inputs[S] = False
            self.slide_timer = 0
            self.sliding = False

        if inputs[A] == True:
            if self.y > 2:
                self.y -= 3

        if inputs[D] == True:
            if self.y < 8:
                self.y += 3


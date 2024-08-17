import math, sys
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
        self.incline = False

    def move(self, inputs, timer):
        
        self.x -= 0.01
        

        if inputs[W] and not self.jumping:
            if self.jumping_timer == 0 or timer - self.jumping_timer > 30:
                self.jumping = True
                inputs[W] = False
                self.jumping_timer = timer
        if self.jumping and timer - self.jumping_timer > 20:
            inputs[W] = False
            #self.jump_timer = 0
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
            inputs[A] = False
            if self.y < 4:
                self.y += 1

        if inputs[D] == True:
            inputs[D] = False
            if self.y > 2:
                self.y -= 1
    
    def is_hit(self, level):
        pass

    def is_incline(self, level):
        if (level[self.y-1][int(self.x)] == 4 or level[self.y-1][int(self.x)]) == 5:
            self.incline = True
        else:
            self.incline = False

    def is_dead(self, level):
        if level[self.y-1][int(self.x)] == 2 and self.x%1 > 0.4 and self.x%1 < 0.6 and not self.jumping:
            return "jump"
        elif level[self.y-1][int(self.x)] == 3 and self.x%1 > 0.4 and self.x%1 < 0.6 and not self.sliding:
            return "slide"

        elif level[self.y-1][int(self.x)] == 5 and self.x%1 > 0.1 and self.x%1 < 0.3 and not self.incline:
            return "fuck"
        else:
            return False

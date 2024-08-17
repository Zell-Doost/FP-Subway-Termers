import math, curses, sys
from player import Player
from sprite import sprites
from obstacles import *


class Render:
    def __init__(self):
        self.ray_angles = []
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        self.colour1 = curses.color_pair(1)
        self.colour2 = curses.color_pair(2)
        self.colour3 = curses.color_pair(3)
        self.colour4 = curses.color_pair(4)
        self.colour5 = curses.color_pair(5)
        self.colour = [self.colour1, self.colour1]
        self.obstacles = []
        self.spawn = 4

    def render_world_bad(self, player, screen, level):
        bottom_middle = (49, 85)
        try:
            for i in range(49, 29, -1):
                for j in range(60, 110):
                    screen.addstr(i, j, rail[i-30][j-60])
        
        except:
            curses.endwin()
            print(i-30, j-60)
            sys.exit()
        rail2 = rail[::len(rail)//16]


    def render_world(self, player, screen, level):
        if player.y - int(player.y) < 0.2:
            self.spawn = int(player.y + 4)
        screen.addstr(0, 0, str(self.spawn))
        for i, j in enumerate(level[self.spawn]):
            if j == '1':
                screen.addstr(0, 0, "test")
                self.obstacles.append(JumpRail(i, self.spawn))
            elif j == '2':
                self.obstacles.append(SlideRail(self.spawn, i))
            elif j == '3':
                self.obstacles.append(Train(self.spawn, i))

        for obstacle in self.obstacles:
            sx = obstacle.x
            sy = 10*(player.y - obstacle.y)

            for i in range(int(sy)):
                for j in range(int(sy)):
                    try:
                        if player.x - sx == 1:
                            screen.addstr(int(i+sy), int((42-(j/2))), "#")
                        if player.x - sx == 0:
                            screen.addstr(int(i+sy), int((85-(j/2))), "#")
                        if player.x - sx == -1:
                            screen.addstr(int(i+sy), int((128-(j/2))), "#")
                    except:
                        pass

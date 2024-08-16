import math, curses, sys
from player import Player


class Render:
    def __init__(self):
        self.ray_angles = []

    def cast_ray(self, player, level, ray_offset, screen):

        #if len(self.ray_angles) == 120:
        #    curses.endwin()
        #    print(self.ray_angles)
        #    sys.exit()
        ray_angle = player.angle + ray_offset*(math.pi/180)
        #if ray_angle < 0:
        #    ray_angle += 2*math.pi
        #if ray_angle > 2*math.pi:
        #    ray_angle -= 2*math.pi
        #if player.angle < 0:
        #    ray_angle += 2*math.pi
        #if player.angle > 2*math.pi:
        #    ray_angle -= 2*math.pi
        ray_x, ray_y, x_offset, y_offset = 0, 0, 0, 0
        hw_ray_length = 1000000000
        hx_ray_length = player.x
        hy_ray_length = player.y
        vw_ray_length = 1000000000
        vx_length = player.x
        vy_length = player.y
        nTan = -math.tan(ray_angle)
        aTan = -1/math.tan(ray_angle)

        
        #Check Vertical Lines
        view_length = 0
        #ray_y, ray_x, y_offset, x_offset = 0, 0, 0, 0
        if ray_angle > math.pi/2 and ray_angle < 3*math.pi/2:
        #if player.angle > math.pi/2 and player.angle < 3*math.pi/2:
            ray_x = int(player.x) - 0.000001
            ray_y = (player.x - ray_x) * nTan + player.y
            x_offset = -1
            y_offset = -x_offset*nTan
        if ray_angle < math.pi/2 or ray_angle > 3*math.pi/2:
        #if player.angle < math.pi/2 or player.angle > 3*math.pi/2:
            ray_x = int(player.x) + 1
            ray_y = (player.x - ray_x) * nTan + player.y
            x_offset = 1
            y_offset = -x_offset*nTan
        if ray_angle == math.pi/2 or ray_angle == 3*math.pi/2:
        #if player.angle == math.pi/2 or player.angle == 3*math.pi/2:
            ray_y = player.y
            ray_x = player.x


        while view_length < 8:
            try:
                if abs(ray_y) <= len(level) and abs(ray_x) <= len(level[0]) and level[int(ray_y)-1][int(ray_x)-1] == 1:
                    view_length = 8
                else:
                    ray_x += x_offset
                    ray_y += y_offset
                    view_length += 1
            except:
                return
                curses.endwin()
                print(f"ray_y: {ray_y}, ray_x: {ray_x}")
        #----------------------------------------------
        #if player.angle > math.pi/2:
            #ray_y += 1
        vx_length = player.x - ray_x
        vy_length = player.y - ray_y
        vw_ray_length = math.sqrt(vx_length**2 + vy_length**2)       



        ##Check Horizontal Walls
        view_length = 0
        ray_y, ray_x, y_offset, x_offset = 0, 0, 0, 0
        if ray_angle > math.pi:
        #if player.angle > math.pi:
            ray_y = int(player.y) - 0.000001
            ray_x = (player.y - ray_y) * aTan + player.x
            y_offset = -1
            x_offset = -y_offset*aTan
        if ray_angle < math.pi:
        #if player.angle < math.pi:
            ray_y = int(player.y) + 1
            ray_x = (player.y - ray_y) * aTan + player.x
            y_offset = 1
            x_offset = -y_offset*aTan
        if ray_angle == 0 or ray_angle == math.pi:
        #if player.angle == 0 or player.angle == math.pi:
            ray_y = player.y
            ray_x = player.x
            view_length = 8


        while view_length < 8:
            try:
                if abs(ray_y) <= len(level) and abs(ray_x) <= len(level[0]) and level[int(ray_y)-1][int(ray_x)-1] == 1:
                    view_length = 8
                else:
                    ray_x += x_offset
                    ray_y += y_offset
                    view_length += 1
            except:
                return
        #if player.angle > math.pi/2:
            #---------------------------------------------
            #ray_x += 1
        hx_length = player.x - ray_x
        hy_length = player.y - ray_y
        hw_ray_length = math.sqrt(hx_length**2 + hy_length**2)



        if hw_ray_length == 0:
            hw_ray_length = 10000000000
        if vw_ray_length == 0:
            vw_ray_length = 10000000000

        #ray_length = min(hw_ray_length, vw_ray_length)
        if vw_ray_length < hw_ray_length:
            ray_x = vx_length
            ray_y = vy_length
        if hw_ray_length < vw_ray_length:
            ray_x = hx_length
            ray_y = hy_length
        ray_length = min(vw_ray_length, hw_ray_length)
        #ray_length = math.sqrt(ray_x**2 + ray_y**2)
        ray_length *= math.cos(player.angle-ray_angle)
        wall_height = 40 / ray_length
        if wall_height > 40:
            wall_height = 40
        vertical_draw = (int(25-wall_height//2), int(wall_height+25-wall_height//2))
        if player.sliding:
            vertical_draw = (int(25-wall_height), 25)
        if player.jumping:
            vertical_draw = (25, int(25+wall_height))
        for i in range(vertical_draw[0], vertical_draw[1]):
            try:
                #Horizontal wall are light, vertical wall are dark
                if abs(ray_angle - player.angle) > 2 and player.angle < math.pi/2:
                    ray_angle -= 2*math.pi
                if abs(ray_angle - player.angle) > 2 and player.angle > 3*math.pi/2:
                    ray_angle += 2*math.pi

                x_graph = int((ray_angle - player.angle) * (180 / math.pi) + 80)
                
                if vw_ray_length > hw_ray_length:
                    screen.addstr(i, x_graph, "#")
                else:
                    screen.addstr(i, x_graph, "#", curses.A_DIM)
            except:
                return
                curses.endwin()
                print(i)
                print(int(ray_angle*(180/math.pi)))
                sys.exit()
                pass







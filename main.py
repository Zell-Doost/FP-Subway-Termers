import curses, os, time, math
from pynput import keyboard
from pynput.keyboard import Key
from player import Player
from renderer import Render

W, S, A, D, Q, E = 1, 2, 3, 4, 5, 6

pressed = {W: False, S: False, A: False, D: False, 
           Q: False, E: False}

level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         #[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
         [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

def on_press(key):
    #if key not in pressed:
    #    pressed.append(key)
    try:
        if key.char == 'w':
            pressed[W] = True
        if key.char == 's':
            pressed[S] = True
        if key.char == 'a':
            pressed[A] = True
        if key.char == 'd':
            pressed[D] = True
    except:
        pass

def on_release(key):
    #while key in pressed:
    #    pressed.remove(key)
    if key == Key.esc:
        return False
    try:
        if key.char == 'w':
            pressed[W] = False
        if key.char == 's':
            pressed[S] = False
        if key.char == 'a':
            pressed[A] = False
        if key.char == 'd':
            pressed[D] = False


    except:
        pass

listener = keyboard.Listener(
        on_press = on_press, 
        on_release = on_release)
listener.start()


def main(stdscr):
    timer = 0
    stdscr.clear()
    player = Player()
    renderer = Render()
    for _ in range(10000):
        player.move(pressed, timer)
        #player.is_incline(level)
        for i in range(50):
            for j in range(169):
                stdscr.addstr(i, j, " ")
        for i in range(-90, 30):
            renderer.cast_ray(player, level, i, stdscr)
        stdscr.refresh()
        timer += 1
        time.sleep(1/60)
        

os.system('resize -s 50 170')
curses.wrapper(main);

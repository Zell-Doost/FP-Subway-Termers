import curses, os, time
from pynput import keyboard
from pynput.keyboard import Key
from player import Player

W, S, A, D, Q, E = 1, 2, 3, 4, 5, 6

pressed = {W: False, S: False, A: False, D: False, 
           Q: False, E: False}
#pressed = []

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
        if key.char == 'q':
            pressed[Q] = True
        if key.char == 'e':
            pressed[E] = True
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
        if key.char == 'q':
            pressed[Q] = False
        if key.char == 'e':
            pressed[E] = False


    except:
        pass

listener = keyboard.Listener(
        on_press = on_press, 
        on_release = on_release)
listener.start()


def main(stdscr):
    
    stdscr.clear()
    player = Player([0, 0])
    for _ in range(1000):
        player.input_handle(pressed)
        player.move()
        stdscr.addstr(0, 0, "                           ")
        stdscr.addstr(1, 0, "                           ")
        stdscr.addstr(0, 0, str(player.inputs))
        stdscr.addstr(1, 0, str(player.position))
        stdscr.refresh()
        time.sleep(1/60)
        

os.system('resize -s 50 170')
curses.wrapper(main);

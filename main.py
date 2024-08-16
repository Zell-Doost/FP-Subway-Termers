import curses, os, time
from pynput import keyboard
from pynput.keyboard import Key


pressed = []


def on_press(key):
    if key not in pressed:
        pressed.append(key)

def on_release(key):
    while key in pressed:
        pressed.remove(key)
    if key == Key.esc:
        return False

listener = keyboard.Listener(
        on_press = on_press, 
        on_release = on_release)
listener.start()


def main(stdscr):
    
    stdscr.clear()
    for _ in range(1000):
        stdscr.addstr(0, 0, "                           ")
        stdscr.addstr(0, 0, str(pressed))
        stdscr.refresh()
        time.sleep(1/60)
        

os.system('resize -s 50 170')
curses.wrapper(main);

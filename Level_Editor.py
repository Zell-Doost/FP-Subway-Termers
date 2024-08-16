import curses
from curses import wrapper


def create_level(x_pos: int, y_pos: int) -> list[list[str]]:
	""" creates a level full of thin air, based on the x and y pos"""
	board = []
	for i in range(y_pos):
		row = []
		for j in range(x_pos):
			row.append("0")
		board.append(row)


	return board


def draw_level(level: list[list[str]], stdscr):
	stdscr.clear()
	for i in level:
		for j in i:
			stdscr.addstr(j)
			#stdscr.addstr(" ")
		stdscr.addstr("\n")


	stdscr.refresh()



def main(stdscr):
	curses.mousemask(1)
	level = create_level(20, 20)
	level[0][10] = "J"
	draw_level(level, stdscr)
	
	while True:
		event = stdscr.getch()
		if event == ord("q"): break
		if event == curses.KEY_MOUSE:
			click = curses.getmouse()
			_, mouse_x, mouse_y, _, _ = click
			if mouse_x < len(level[0]) and mouse_y < len(level):
				level[mouse_y][mouse_x] = "1"
				draw_level(level, stdscr)
			stdscr.addstr(30, 30, str(click))
			stdscr.refresh()
	stdscr.refresh()
	stdscr.getch()




wrapper(main)

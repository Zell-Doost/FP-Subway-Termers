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




def main(stdscr):
	curses.mousemask(1)
	level = create_level(20, 20)
	level[0][10] = "J"
	stdscr.clear()
	for i in level:
		for j in i:
			stdscr.addstr(j)
			stdscr.addstr(" ")
		stdscr.addstr("\n")

	stdscr.refresh()
	stdscr.getch()
	while True:
		event = stdscr.getch()
		if event == ord("q"): break
		if event == curses.KEY_MOUSE:
			click = curses.getmouse()
			stdscr.addstr(30, 30, str(click))
			stdscr.refresh()
	stdscr.refresh()
	stdscr.getch()




wrapper(main)

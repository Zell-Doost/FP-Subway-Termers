import curses
from curses import wrapper


def create_level(x_pos: int, y_pos: int) -> list[list[str]]:
	""" creates a level full of thin air, based on the x and y pos"""
	board = []
	for i in range(y_pos):
		row = []
		for j in range(x_pos):
			if i in [0, y_pos-1] or j in [0, x_pos-1]:
				tile = "1"
			else:
				tile = "0"
			row.append(tile)
		board.append(row)


	return board


def draw_level(level: list[list[str]], stdscr, editor_mode: str):
	stdscr.clear()
	for i in level:
		for j in i:
			stdscr.addstr(j)
			stdscr.addstr(" ")
		stdscr.addstr("\n")
	stdscr.addstr("\n")
	colour_map = {"1": curses.A_BOLD, "2": curses.A_BOLD, "3": curses.A_BOLD, "0": curses.A_BOLD, "4": curses.A_BOLD}
	colour_map[editor_mode] = curses.A_STANDOUT
	stdscr.addstr("modes (press key to change input): " + "\n")
	stdscr.addstr("0: floor ", colour_map["0"])
	stdscr.addstr(" 1: wall ", colour_map["1"])
	stdscr.addstr(" 2: door ", colour_map["2"])
	stdscr.addstr(" 3: enemy ", colour_map["3"])
	stdscr.addstr(" 4: move/add player character", colour_map["4"])
	

def mode(character: int) -> str:
	#wall
	if character == ord("1"):
		return "1"
	#door
	if character == ord("2"):
		return "2" #placeholder
	#enemy placeholder
	if character == ord("3"):
		return "3"
	if character == ord("4"):
		return "4"
	else:
		return "0"

		
		
	

def main(stdscr):
	editor_mode = mode(0)
	
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
	curses.mousemask(1)
	level = create_level(10, 20)

	while True:
		draw_level(level, stdscr, editor_mode)
		stdscr.refresh()
		event = stdscr.getch()
		if event == ord("q"): break
		if event == curses.KEY_MOUSE:
			click = curses.getmouse()
			_, mouse_x, mouse_y, _, _ = click
			level_mouse_x = mouse_x/2
			
			if level_mouse_x.is_integer() and level_mouse_x < len(level[0]) and mouse_y < len(level):
				if editor_mode == "4":
					for i in range(len(level)):
						for j in range(len(level[i])):
							if level[i][j] == "4":
								level[i][j] = "0"


				level[mouse_y][int(level_mouse_x)] = editor_mode
			stdscr.addstr(30, 30, str(click))
		else:
			editor_mode = mode(event)
			stdscr.refresh()

			
	stdscr.refresh()




wrapper(main)

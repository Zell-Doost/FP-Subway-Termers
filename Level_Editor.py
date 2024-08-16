import curses
import time
from curses import wrapper
from curses.textpad import Textbox, rectangle 



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

def draw_level(level: list[list[str]], stdscr):
	for i in level:
		for j in i:
			stdscr.addstr(j)
			stdscr.addstr(" ")
		stdscr.addstr("\n")
	stdscr.addstr("\n")


def draw_hud(level: list[list[str]], stdscr, editor_mode: str):
	stdscr.clear()
	draw_level(level, stdscr)
	colour_map = {"1": curses.A_BOLD, "2": curses.A_BOLD, "3": curses.A_BOLD, "0": curses.A_BOLD, "4": curses.A_BOLD}
	colour_map[editor_mode] = curses.A_STANDOUT
	stdscr.addstr("modes (press key to change input): " + "\n")
	stdscr.addstr("0: floor ", colour_map["0"])
	stdscr.addstr(" 1: wall ", colour_map["1"])
	stdscr.addstr(" 2: door ", colour_map["2"])
	stdscr.addstr(" 3: enemy ", colour_map["3"])
	stdscr.addstr(" 4: move/add player character " + "\n", colour_map["4"])
	if editor_mode == "l":
		stdscr.clear()
		stdscr.addstr("filename (ctr + g to exit) (make sure it is in the level directory): ")
		win = curses.newwin(3, 18, 2, 2)
		box = Textbox(win)
		rectangle(stdscr, 1, 1, 5, 20)
		stdscr.refresh()
		box.edit()
		text = box.gather()[:-2:]
		directory = "Levels/" + text + ".txt"
		newlevel = []
		try:
			file = open(directory, "r")
			for line in file:
				row = [tile for tile in line if tile != '\n']
				newlevel.append(row)
			file.close()
			stdscr.clear()
			draw_level(newlevel, stdscr)
			stdscr.addstr("file loaded from  " + directory + " (press any key to continue)")
			return newlevel


		except FileNotFoundError:
			stdscr.clear()
			draw_level(level, stdscr)
			stdscr.addstr(directory + " does not exist (press any key to continue)")

	if editor_mode == "s":
		stdscr.clear()
		stdscr.addstr("filename (ctr + g to exit) (to be saved to level directory): ")
		win = curses.newwin(3, 18, 2, 2)
		box = Textbox(win)


		rectangle(stdscr, 1, 1, 5, 20)
		stdscr.refresh()
		box.edit()
		text = box.gather()[:-2:]
		directory = "Levels/" + text + ".txt"
		file = open(directory, "w")
		for i in level:
			for j in i:
				file.write(j)
			file.write("\n")
		file.close()
		stdscr.clear()
		draw_level(level, stdscr)
		stdscr.addstr("file saved in " + directory + " (press any key to continue)")
	return level




	

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
	if character == ord("l"):
		return "l"
	if character == ord("s"):
		return "s"
	else:
		return "0"


		

	

def main(stdscr):
	editor_mode = mode(0)
	
	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW)
	curses.mousemask(1)
	level = create_level(20, 20)

	while True:
		stdscr.clear()
		level = draw_hud(level, stdscr, editor_mode)
		stdscr.refresh()
		buttons = curses.newwin(15, 12, len(level)//3, 2*len(level[0])+10)
		buttons.addstr("|Press s to|| save game|")
		for i in range(len(level)//3):
			buttons.addstr("\n")
		buttons.addstr("|Press l to|| load game|")
		buttons.refresh()
		stdscr.addstr(len(level) + 3, 0, "")
		stdscr.refresh()
		event = stdscr.getch()
		if event == ord("q"): break
		elif event == curses.KEY_MOUSE:
			click = curses.getmouse()
			stdscr.addstr(40, 40, str(click))
			_, mouse_x, mouse_y, _, _ = click
			level_mouse_x = mouse_x/2
			
			if level_mouse_x.is_integer() and level_mouse_x < len(level[0]) and mouse_y < len(level):
				if editor_mode == "4":
					for i in range(len(level)):
						for j in range(len(level[i])):
							if level[i][j] == "4":
								level[i][j] = "0"


				level[mouse_y][int(level_mouse_x)] = editor_mode
		else:
			editor_mode = mode(event)
		stdscr.refresh()


			
	stdscr.refresh()




wrapper(main)

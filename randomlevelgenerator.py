import random
import curses
import time
from curses import wrapper
from curses.textpad import Textbox, rectangle 

def random_tiles() -> list[str]:
	possible_game_sprites = ["00001", "00010", "00200", "00000", "10000", "00020", "00100", "03455", "05555", "00010"]
	tile_0 = random.choices(possible_game_sprites)
	tile_1 = random.choices(possible_game_sprites)
	tile_2 = random.choices(possible_game_sprites)
	if tile_0 == tile_1 and tile_1 == tile_2:
		random_tiles()
	return [tile_0, tile_1, tile_2]




def main(stdscr):
	game_rows = [[], [], []]
	possible_game_sprites = ["00000", "00010", "00200", "00000", "00000", "00020", "00100", "03455", "05555", "00010"]
	for i in range(20):
		tileset = random_tiles()
		for j in range(1):
			game_rows[0].extend(tileset[0][j])
			game_rows[1].extend(tileset[1][j])
			game_rows[2].extend(tileset[2][j])

	print(game_rows)

	stdscr.clear()

	for i in game_rows:
		for j in i:
			stdscr.addstr(j)
			stdscr.addstr("")
		stdscr.addstr("\n")
	stdscr.addstr("\n")
	stdscr.refresh()
	stdscr.getch()


wrapper(main)
if __name__ == "__main__":
	main()




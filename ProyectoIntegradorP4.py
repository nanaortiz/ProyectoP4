import os
import readchar
from typing import List, Tuple

WALL = "#"
PATH = "."
PLAYER = "P"

def crear_laberinto_desde_cadena(maze_string: str, start: Tuple[int, int], end: Tuple[int, int]) -> List[List[str]]:
    maze = [list(row) for row in maze_string.strip().split("\n")]

    # punto de icicio y final
    maze[start[1]][start[0]] = PLAYER
    maze[end[1]][end[0]] = PATH

    return maze


def print_maze(maze: List[List[str]]) -> None:
    os.system('cls' if os.name == 'nt' else 'clear')  # 2. Limpiar pantalla
    for row in maze:
        print("".join(row))


def main_loop(maze: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]) -> None:
    px, py = start

    while (px, py) != end:
        print_maze(maze)
        key = readchar.readkey()

        if key == "q":
            break
        elif key.lower() == "a" or key == readchar.key.LEFT:
            if px - 1 >= 0 and maze[py][px - 1] != WALL:
                maze[py][px] = PATH
                px -= 1
                maze[py][px] = PLAYER
        elif key.lower() == "s" or key == readchar.key.DOWN:
            if py + 1 < len(maze) and maze[py + 1][px] != WALL:
                maze[py][px] = PATH
                py += 1
                maze[py][px] = PLAYER
        elif key.lower() == "d" or key == readchar.key.RIGHT:
            if px + 1 < len(maze[0]) and maze[py][px + 1] != WALL:
                maze[py][px] = PATH
                px += 1
                maze[py][px] = PLAYER
        elif key.lower() == "w" or key == readchar.key.UP:
            if py - 1 >= 0 and maze[py - 1][px] != WALL:
                maze[py][px] = PATH
                py -= 1
                maze[py][px] = PLAYER


if __name__ == "__main__":
    # Configuración del laberinto generado
    maze_string = """
    ####################
    #..................#
    #.################.#
    #.#..............#.# 
    #.#.############.#.#
    #.#..............#.# 
    #.################.#
    #..................#
    ####################
    """

    start_position = (0, 0)
    end_position = (17, 8)

    maze = crear_laberinto_desde_cadena(maze_string, start_position, end_position)
    main_loop(maze, start_position, end_position)
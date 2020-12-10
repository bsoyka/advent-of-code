import curses
import time


def main(stdscr):
    stdscr.clear()
    grid = {}
    with open("input.txt") as f:
        for line_index, line in enumerate(f.readlines()):
            row = line.strip()
            grid[str(line_index)] = {
                str(char_index): char
                for char_index, char in enumerate([char for char in row])
            }
    loc = [25 // 2, 25 // 2]
    facing = "N"
    done = 0
    infections = 0

    def update():
        for i in range(25):
            stdscr.addstr(
                i + 1,
                1,
                " " + " ".join([grid[str(i)][str(x)] for x in range(25)]) + " ",
            )
        if 0 <= loc[0] <= 24 and 0 <= loc[1] <= 24:
            stdscr.addstr(loc[1] + 1, (loc[0] * 2) + 1, "[")
            stdscr.addstr(loc[1] + 1, (loc[0] * 2) + 3, "]")
        stdscr.addstr((25 // 2) - 6, (25 * 2) + 4, "Facing:", curses.A_BOLD)
        stdscr.addstr((25 // 2) - 5, (25 * 2) + 4, facing)
        stdscr.addstr((25 // 2) - 2, (25 * 2) + 4, "Location:", curses.A_BOLD)
        stdscr.addstr((25 // 2) - 1, (25 * 2) + 4, str(loc) + "     ")
        stdscr.addstr((25 // 2) + 2, (25 * 2) + 4, "Done:", curses.A_BOLD)
        stdscr.addstr((25 // 2) + 3, (25 * 2) + 4, str(done))
        stdscr.addstr((25 // 2) + 6, (25 * 2) + 4, "Infections:", curses.A_BOLD)
        stdscr.addstr((25 // 2) + 7, (25 * 2) + 4, str(infections), curses.A_STANDOUT)
        stdscr.refresh()

    update()

    for _ in range(10_000):
        x = loc[0]
        y = loc[1]
        try:
            if grid[str(y)][str(x)] == "#":
                if facing == "N":
                    facing = "E"
                elif facing == "E":
                    facing = "S"
                elif facing == "S":
                    facing = "W"
                elif facing == "W":
                    facing = "N"
            elif grid[str(y)][str(x)] == ".":
                if facing == "N":
                    facing = "W"
                elif facing == "W":
                    facing = "S"
                elif facing == "S":
                    facing = "E"
                elif facing == "E":
                    facing = "N"
        except:
            if facing == "N":
                facing = "W"
            elif facing == "W":
                facing = "S"
            elif facing == "S":
                facing = "E"
            elif facing == "E":
                facing = "N"
        update()
        try:
            if grid[str(y)][str(x)] == "#":
                grid[str(y)][str(x)] = "."
            elif grid[str(y)][str(x)] == ".":
                grid[str(y)][str(x)] = "#"
                infections += 1
        except:
            grid[str(y)][str(x)] = "#"
            infections += 1
        update()
        try:
            grid[str(loc[1] - 1)] = grid[str(loc[1] - 1)]
        except:
            grid[str(loc[1] - 1)] = {}
        try:
            grid[str(loc[1] + 1)] = grid[str(loc[1] + 1)]
        except:
            grid[str(loc[1] + 1)] = {}
        if facing == "N":
            loc = [loc[0], loc[1] - 1]
        elif facing == "E":
            loc = [loc[0] + 1, loc[1]]
        elif facing == "S":
            loc = [loc[0], loc[1] + 1]
        elif facing == "W":
            loc = [loc[0] - 1, loc[1]]
        update()
        done += 1
    time.sleep(100)


curses.wrapper(main)

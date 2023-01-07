import curses
import time

from .logger import Logger


class ImageEngine(Logger):
    """
    TODO - Simple exmplanation on how to use
    """

    TICK_TIME = 1  # Time it takes to refresh a frame
    PIXEL = "\u2588"  # Creates a solid block => █
    COLOR_COUNT = 0  # Index for colors
    COLORS = {}

    def __init__(self, curse) -> None:
        self.c = curse
        curses.curs_set(0)  # Disable cursor
        self.c.nodelay(1)  # Start without user action
        curses.start_color()
        curses.use_default_colors()

        y, x = self.c.getmaxyx()
        self.max_y = y - 1
        self.max_x = x - 2
        self.log(f"x:{self.max_x}, y:{self.max_y}")

    def exit(self) -> None:
        """
        Closes the program if the user presses the letter q.
        """
        try:
            if chr(self.c.getch()) == "q":
                exit()
        except ValueError:
            pass

    def loop(self) -> None:
        self.exit()
        time.sleep(self.TICK_TIME)
        self.c.refresh()

    def create_rgb_color(self, name: str, r: int, g: int, b: int) -> None:
        if self.COLOR_COUNT == 255:
            self.COLOR_COUNT = 0

        if name not in self.COLORS.keys():
            self.COLOR_COUNT += 1
            self.COLORS[name] = self.COLOR_COUNT
            # Create the color on curses
            curses.init_color(
                self.COLOR_COUNT,
                (r * 1000) // 255,
                (g * 1000) // 255,
                (b * 1000) // 255,
            )
            curses.init_pair(self.COLOR_COUNT, self.COLOR_COUNT, curses.COLOR_BLACK)

    def paint_pixel(self, x: int, y: int, color_name: str) -> None:
        """
        X = left to right\n
        Y = up to down\n
        (Starts always at the top left corner)
        """
        self.c.attron(curses.color_pair(self.COLORS[color_name]))
        self.c.addstr(y, x, self.PIXEL)

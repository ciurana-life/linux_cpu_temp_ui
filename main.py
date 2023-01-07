import curses

from linux_cpu_temp_ui.system import cpu_temp
from linux_cpu_temp_ui.image_engine import ImageEngine
from linux_cpu_temp_ui.fonts import Fonts as F


def main(c):
    IE = ImageEngine(c)
    IE.create_rgb_color("white", 200, 200, 200)
    IE.create_rgb_color("red", 200, 0, 0)
    IE.create_rgb_color("green", 50, 200, 50)
    IE.create_rgb_color("yellow", 200, 200, 51)
    IE.create_rgb_color("orange", 255, 165, 0)

    while True:
        # Every frame start by clearing
        c.clear()

        # Get temperature
        temp = cpu_temp()
        _temp = int(temp)

        # Assign color to temperature
        color = "white"
        if _temp > 50:
            color = "green"
        if _temp > 60:
            color = "yellow"
        if _temp > 70:
            color = "orange"
        if _temp > 80:
            color = "red"

        # +100 degrees so you are fucked
        if len(temp) >= 3:
            IE.paint_pixel(0, 0, "red")
            break

        # Paint the temperature
        digits, n = [*temp], 0

        # We have 2 digits
        for digit in digits:

            # Get the "font"
            digit_matrix = eval(f"F._{digit}")
            # Displace 8 points the x value if is the first number
            displace = 8 if n == 1 else 0
            
            # Paint every "pixel"
            for ln, line in enumerate(digit_matrix):
                for pn, point in enumerate(line):
                    x = pn + displace + 2
                    y = ln + 2
                    if point == 1:
                        IE.paint_pixel(x, y, color)
            n += 1

        # Sleep
        IE.loop()


if __name__ == "__main__":
    curses.wrapper(main)

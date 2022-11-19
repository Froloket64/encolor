## Graphical backend ##

## TODO:
# - Windows escape sequence
# - Add background coloring

ESCAPE = "\033"
COLOR_NAMES = ["black", "red", "green", "yellow", "blue", "purple", "aqua", "gray"]

class Rgb:
    # r: int
    # g: int
    # b: int
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.b = b
        self.g = g

    def __repr__(self):
        return f"Rgb({self.r}, {self.g}, {self.b})"

    def __eq__(self, other):
        return (self.r, self.g, self.b) == (other.r, other.g, other.b)

    def to_hex(self, short=False):
        if short:
            if any(c % 17 for c in (self.r, self.g, self.b)):
                raise ValueError("Can't convert to short")

            return f"#{self.r // 17:x}{self.g // 17:x}{self.b // 17:x}"

        return f"#{self.r:0>2x}{self.g:0>2x}{self.b:0>2x}"

    @classmethod
    def from_hex(cls, color: str):
        """
        Return an Rgb instance from hex string

        color  - HEX-encoded color string
        """

        if not cls.is_hex(color):
            raise ValueError(f"Invalid HEX syntax: {color}")

        color = color.strip("#")

        # NOTE: No `match` for better version compat
        if len(color) == 6: # Full HEX
            r, g, b = color[:2], color[2:4], color[4:]

        elif len(color) == 3: # Short HEX
            r, g, b = color[0]*2, color[1]*2, color[2]*2

        return Rgb(int(r, 16), int(g, 16), int(b, 16))

    @classmethod
    def is_hex(cls, color: str):
        """
        Check if a string is a valid HEX value
        """

        color = color.strip("#")

        return len(color) in (3, 6) and all(char.isdigit() or char in "abcdef" for char in color)

def colorize(s: str, color: Rgb):
    """
    Return a string with escape sequence coloring applied

    s      - String to colorize
    color  - Color in RGB (3-element collection)
    """

    return f"{ESCAPE}[38;2;{color.r};{color.g};{color.b}m{s}{ESCAPE}[0m"

def colorize_ansi(s: str, name: str, bright=False):
    """
    Return a terminal color by its name

    name    - Name of the color from everyday English
    bright  - Whether the bright version should be returned
    """

    color = COLOR_NAMES.index(name) + bright*8

    return f"{ESCAPE}[38;5;{color}m{s}{ESCAPE}[0m"

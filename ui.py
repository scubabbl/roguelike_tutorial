import abc
import tdl

class UI(abc.ABC):
    def __init__(self ,console, size, destination, fg, bg):
        self.console = console
        self.width, self.height = size
        self.x, self.y = destination
        self.fg = fg
        self.bg = bg
        self.window = tdl.Window(self.console, self.x, self.y, self.width, self.height)
        self.width, self.height = self.window.get_size()
        self.window.set_colors(fg=self.fg, bg=self.bg)


from game import Game
from ui import UI
import colors

class MapUI(UI):
    def __init__(self, console, size, destination):
        self.fg = colors.lightest_green
        self.bg = colors.dark_gray
        super().__init__(console, size, destination, self.fg, self.bg)
        self.default_char = '.'
        self.tiles = None

    def draw(self):
        self._fill()

    def _fill(self):
        self.window.draw_rect(0, 0, None, None, None)
    
    def clear(self):
        self.tiles = None
        self.window.clear(fg=self.fg, bg=self.bg)


class MessageUI:
    def __init__(self, console, size, destination):
        self.fg = colors.lightest_green
        self.bg = colors.dark_gray
        super().__init__(console, size, destination, self.fg, self.bg)

class UIManager:
    def __init__(self, game, size):
        self.game = game
        self.console = self.game.root_console
        assert self.console is not None
        self.width, self.height = size
        self.size = size
        self.windows = []

    def layout_ui(self):
        self.create_map_ui(size=self.size, destination=(0,0))
    
    def create_map_ui(self, size, destination):
        self.map_ui = MapUI(self.console, size=size, destination=destination)
        self.windows.append(self.map_ui)
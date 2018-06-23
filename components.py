####################################
## Components
####################################
class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self):
        self.vx = 0
        self.vy = 0

class Renderable:
    def __init__(self, char):
        self.char = char

class Player:
    def __init__(self):
        pass
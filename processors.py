import esper
import tdl
from components import *

####################################
## Processors
####################################
class VelocityProcessor(esper.Processor):
    def __init__(self):
        pass
    
    def process(self):
        for ent, (vel, pos) in self.world.get_components(Velocity, Position):
            if vel.vx != 0 or vel.vy != 0:
                pos.x = pos.x + vel.vx
                pos.y = pos.y + vel.vy
                vel.vx = 0
                vel.vy = 0

    def handle(self, action):
        print("Handling %s" % action)
        dir = action.get("MOVE")
        if dir is not None:
            for ent, (vel, player) in self.world.get_components(Velocity, Player):
                if dir == "NORTH":
                    vel.vx, vel.vy = 0,-1
                elif dir == "SOUTH":
                    vel.vx, vel.vy = 0,1
                elif dir == "EAST":
                    vel.vx, vel.vy = 1, 0
                elif dir == "WEST":
                    vel.vx, vel.vy = -1, 0


class MainRenderProcessor(esper.Processor):
    def __init__(self, root_console):
        self.root_console = root_console
    
    def process(self):
        for ent, (pos, rend) in self.world.get_components(Position, Renderable):
            self.root_console.draw_char(pos.x, pos.y, rend.char, bg=None, fg=(255, 255, 255))

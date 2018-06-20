import tdl
import logging
import esper
from input_handler import InputHandler as IH
import time
from action_dispather import ActionDispatcher as AD

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


####################################
## Core Game
####################################
class Game:
    def __init__(self):
        logging.debug("Game initializing")
        self.world = None
        self.screen_width = 80
        self.screen_height = 50
        self.root_console = None
    

    def initialize_world(self):
        self.world = esper.World()
        self.player = self.world.create_entity(Position(40, 25), Renderable('@'), Player(), Velocity())    
        render_processor = MainRenderProcessor(self.root_console)
        velocity_processor = VelocityProcessor()
        self.world.add_processor(render_processor)
        self.world.add_processor(velocity_processor, priority=1)
        self.action_dispatcher = AD(self, [velocity_processor])


    def run(self):
        logging.debug("Game running")
        tdl.set_font('arial10x10.png', greyscale=True, altLayout=True)
        self.root_console = tdl.init(self.screen_width, self.screen_height, title="Testing")
        self.initialize_world()
        
        self.running = True

        while self.running and not tdl.event.is_window_closed():
            self.world.process()
            tdl.flush()
            _inputs = list(tdl.event.get())
            for _input in _inputs:
                action = IH.handle(_input)
                break
            else:
                action = {}
            _exit = action.get('EXIT')
            if _exit:
                self.running = False
            if action:
                self.action_dispatcher.handle(action)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Main app starting")
    game = Game()
    game.run()
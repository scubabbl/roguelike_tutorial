import tdl
import logging
import esper
from input_handler import InputHandler as IH
import time
from action_dispather import ActionDispatcher as AD
from processors import *
from components import *



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

            self.world.process()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("Main app starting")
    game = Game()
    game.run()
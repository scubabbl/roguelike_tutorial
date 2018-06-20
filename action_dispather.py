class ActionDispatcher:
    def __init__(self, game ,subscribers):
        self.game = game
        self.subscribers = subscribers
        self.current_priority = None

    def handle(self, action):
        for subscriber in self.subscribers:
            result = subscriber.handle(action)
            if result == None:
                break
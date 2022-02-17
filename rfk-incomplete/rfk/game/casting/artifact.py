from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!


class Artifact(Actor):
    "Provides a message when the robot touches an artifact "

    def __init__(self):
        super().__init__()
        self.message = ""

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!


class Artifact(Actor):
    """Provides a message when the robot touches an artifact 
    Attributes:
        Actor class attributes
        message (message): string message to display"""

    def __init__(self):
        super().__init__()
        self.message = ""

    def get_message(self):
        """Gets the artifact's message
        Returns:
            string: The artifact's message """
        return self.message

    def set_message(self, message):
        """Updates the message to the given value
        Args:
            message (string): The given value."""
        self.message = message

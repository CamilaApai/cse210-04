from game.casting.actor import Actor

class Artifact(Actor):
    """Outputs the game points. 
    
    The responsibility of Artifact is to calculate the game points.

    Attributes:
        _points (int): The game points
    """
    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._points = 0

    def get_points(self):   
        """Calculates the points that the player receives based on what touches.
        
        Returns: The points
        """    
        if (self.get_text() == "*"):
            self._points = 1
        else:
            self._points = -1

        return self._points
    
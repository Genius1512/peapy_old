class Component:
    """
    PeaPy component class
    """

    def __init__(self):
        """
        Construct a new Component object
        """
        self.object_name = None
        self.peapy = None

    def init_(self, game, object_name):
        """
        Called when the component is added to an object.

        Args:
            game (Game): The game object
            object_name (str): The name of the object
        """
        self.peapy = game
        self.object_name = object_name

        try:
            self.peapy = self.init(self.peapy, self.object_name)
        except AttributeError:
            pass

    def init(self, game, object_name: str):
        pass

    def update_(self, game, object_name):
        """
        Called when the component is updated.

        Args:
            game (Game): The game object
            object_name (str): The name of the object
        """
        self.peapy = game
        self.object_name = object_name

        # Update component
        try:
            self.peapy = self.update(self.peapy, self.object_name)
        except AttributeError:
            pass

        return self.peapy

    def update(self, game, object_name: str):
        pass

        return self.peapy

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"

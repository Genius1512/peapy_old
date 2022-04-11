import os
from sys import argv

MAIN = """import peapy


def main():
    game = peapy.PeaPy()

    while game.update():
        pass


if __name__ == "__main__":
    main()

"""

OBJECT_TEMPLATE = """import peapy


class {name}(peapy.Object):
    def __init__(self, name: str):
        super().__init__(name)

    # Called when the object is created
    def init(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Init object

        return self.peapy

    # Called every frame
    def update(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game #  The parent PeaPy object

        # Update object

        return self.peapy
"""


COMPONENT_TEMPLATE = """import peapy


class {name}(peapy.Component):
    def __init__(self):
        super().__init__()

    # Called when the component is created
    def init(self, game: peapy.PeaPy, object_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.object_name = object_name

        # Init component

        return self.peapy

    # Called every frame
    def update(self, game: peapy.PeaPy, object_name: str) -> peapy.PeaPy:
        self.peapy = game # The parent PeaPy object
        self.obj_name = object_name # The name of the parent object

        # Update component

        return self.peapy
"""


def main(args):
    try:
        if args[1] == "init":
            print("Initializing new PeaPy project...")
            with open("main.py", "w") as f:
                f.write(MAIN)
            os.mkdir("assets")
            os.mkdir("assets/images")
            os.mkdir("assets/sounds")
            print("Done!")

        elif args[1] == "new":
            try:
                if args[2] == "object":
                    try:
                        print("Creating new object {}".format(args[3]))
                        with open(args[3].lower() + ".py", "w") as f:
                            f.write(OBJECT_TEMPLATE.format(name=args[3]))
                    except IndexError:
                        print("Please specify a name for the object")

                elif args[2] == "component":
                    try:
                        print("Creating new component {}".format(args[3]))
                        with open(args[3].lower() + ".py", "w") as f:
                            f.write(COMPONENT_TEMPLATE.format(name=args[3]))
                    except IndexError:
                        print("Please specify a name for the component")

            except IndexError:
                print("Please specify the type of component you want to create.")
    except IndexError:
        print("Use either init or new")


if __name__ == "__main__":
    main(argv)

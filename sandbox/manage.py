from argparse import ArgumentParser, Namespace
import os


OBJECT_TEMPLATE = """import peapy


class {name}(peapy.Object):
    def __init__(self, name: str):
        super().__init__(name)

    def init(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Init object

        return self.peapy

    def update(self, game: peapy.PeaPy) -> peapy.PeaPy:
        self.peapy = game

        # Update object

        return self.peapy
"""


COMPONENT_TEMPLATE = """import peapy



class {name}(peapy.Component):
    def __init__(self):
        super().__init__()

    def init(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Init component

        return self.peapy

    def update(self, game: peapy.PeaPy, obj_name: str) -> peapy.PeaPy:
        self.peapy = game
        self.obj_name = obj_name

        # Update component

        return self.peapy
"""


def parse_args() -> Namespace:
    parser = ArgumentParser(description='Manage PeaPy projects')

    # Args
    parser.add_argument(
        "action",
        choices=["new_object", "new_component"],
        help="Action to perform"
    )
    parser.add_argument(
        "name",
        help="Name of the object"
    )

    parser.add_argument(
        "dir",
        default=".",
        help="Directory to create the object in"
    )

    return parser.parse_args()


def main():
    args = parse_args()

    if args.action == "new_object":
        template = OBJECT_TEMPLATE
    elif args.action == "new_component":
        template = COMPONENT_TEMPLATE

    with open(os.path.join(args.dir, args.name.lower() + ".py"), "w") as f:
        f.write(template.format(name=args.name))


if __name__ == "__main__":
    main()


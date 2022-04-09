import os


def main():
    paths = os.listdir("peapy")

    lines = 0

    for path in paths:
        if not os.path.isdir(os.path.join("peapy", path)):
            lines += len(open(os.path.join("peapy", path), "r").read().split("\n"))

    print(lines)


if __name__ == "__main__":
    main()

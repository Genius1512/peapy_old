from datetime import datetime
from rich import print


class Logger:
    def __init__(self, name: str, file_path: str = "stdout"):
        self.name = name
        self.file_path = file_path

    def info(self, *objects):
        out = self.__get_log_string(*objects, level="INFO")
        if self.file_path == "stdout":
            print(f"[white]{out}")
        else:
            with open(self.file_path, "a") as f:
                f.write(out + "\n")

    def warning(self, *objects):
        out = self.__get_log_string(*objects, level="WARNING")
        if self.file_path == "stdout":
            print(f"[yellow]{out}")
        else:
            with open(self.file_path, "a") as f:
                f.write(out + "\n")

    def error(self, *objects):
        out = self.__get_log_string(*objects, level="ERROR")
        if self.file_path == "stdout":
            print(f"[red]{out}")
        else:
            with open(self.file_path, "a") as f:
                f.write(out + "\n")

    def __get_log_string(self, *objects, level: str):
        out = ""
        for obj in objects:
            out += str(obj) + " "
        out = out[:-1]

        return f"[{datetime.now()}][{level}] {self.name}: {out}"

    def __repr__(self):
        return f"peapy.Logger({self.name})"

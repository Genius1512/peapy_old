from typing import Any


class Config:
    def __init__(self, config: dict) -> None:
        for key, value in config.items():
            if type(value) is dict:
                self.__dict__[key] = Config(value)
            else:
                self.__dict__[key] = value

    def __getattr__(self, name: str) -> Any:
        try:
            return self.__dict__[name]
        except KeyError:
            return None

    def __setattr__(self, name: str, value: Any) -> None:
        self.__dict__[name] = value

    def __getitem__(self, key: str) -> Any:
        try:
            return self.__dict__[key]
        except KeyError:
            return None

    def __setitem__(self, key: str, value: Any) -> None:
        self.__dict__[key] = value

    def to_string(self, tabbing: int = 0) -> str:
        out = ""
        for key, value in self.__dict__.items():
            if type(value) is Config:
                out += ("\t" * tabbing) + key + ":\n"
                out += value.to_string(tabbing + 1)
            else:
                out += "\t" * tabbing + f"{key}: {value}\n"
        return out

    def __str__(self) -> str:
        return self.to_string()


def get_default_config() -> Config:
    return Config(
        {
            "window": {
                "width": 800,
                "height": 600,
                "caption": "PeaPy",
                "background": (255, 255, 255),
            },
            "stats": {"max_fps": 60},
            "logger": {"name": "PeaPy", "default_path": "stdout"},
        }
    )


if __name__ == "__main__":
    print(get_default_config())

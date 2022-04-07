import mouse


VALID_BUTTONS = [
    "left",
    "middle",
    "right"
]


def is_pressed(button):
    if button not in VALID_BUTTONS:
        raise ValueError("Invalid button: {}".format(button))
    return mouse.is_pressed(button)


def get_pressed_buttons():
    buttons = []
    for button in VALID_BUTTONS:
        if is_pressed(button):
            buttons.append(button)
    return buttons

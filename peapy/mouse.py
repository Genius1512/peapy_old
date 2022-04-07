import mouse


VALID_BUTTONS = ["left", "middle", "right"]


def is_pressed(button):
    """
    Checks if a mouse button is pressed.

    Args:
        button (str): The button to check. Valid buttons: left, middle, right
    """
    if button not in VALID_BUTTONS:
        raise ValueError("Invalid button: {}".format(button))
    return mouse.is_pressed(button)


def get_pressed_buttons():
    """
    Get all supported buttons that are currently pressed
    """
    buttons = []
    for button in VALID_BUTTONS:
        if is_pressed(button):
            buttons.append(button)
    return buttons

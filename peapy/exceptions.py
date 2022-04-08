class DuplicateObjectException(Exception):
    """
    Raised when trying to create an object that already exists.
    """

    pass


class ObjectNotFoundException(Exception):
    """
    Raised when trying to access an object that doesn't exist.
    """

    pass


class DuplicateComponentException(Exception):
    """
    Raised when trying to create a component that already exists.
    """

    pass


class ComponentNotFoundException(Exception):
    """
    Raised when trying to access a component that doesn't exist.
    """

    pass


class ComponentMissingException(Exception):
    """
    Raised when an object is required to have a certain component, but it doesn't.
    """

    pass

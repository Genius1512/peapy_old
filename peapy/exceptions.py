class DuplicateObjectException(Exception):
    """
    Raised when an object is added to a collection that already contains it.
    """


class ObjectNotFoundException(Exception):
    """
    Raised when an object is not found in a collection.
    """


class DuplicateComponentException(Exception):
    """
    Raised when a component is added to an object that already contains it.
    """


class ComponentNotFoundException(Exception):
    """
    Raised when a component is not found in an object.
    """


class RequiredComponentNotPresent(Exception):
    """
    Raised when a required component is not found in an object.
    """

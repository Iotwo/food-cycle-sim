import logging

from classes.basic_object import BasicObject


logger = logging.getLogger(__name__)


class Lighter(BasicObject):
    """
    DESCR: This class represents all movable objects in model
    """

    @BasicObject._general_logger
    def __init__(self, position_x: int, position_y: int, light_power: int) -> None:
        logger.debug(f"Object {self} at {id(self)} calling ancestor's method \"{super(object, self).__init__.__name__}\".")
        super(Lighter, self).__init__(position_x, position_y)

        self.power = light_power

        self.tile = 'O'

        return None

    def __new__(cls, *args, **kwargs) -> BasicObject:
        instance = super(Lighter, cls).__new__(cls, *args, **kwargs)

        instance.power = None

        return instance

    
    @BasicObject._general_logger
    def get_position(self,) -> tuple:
        """
        DESCR: Return current object set of coordinates
        RETURN: tuple (coordinate X, coordinate Y)
        """
        return (self.x, self.y,)

    @BasicObject._general_logger
    def set_position(self, position_x: int, position_y) -> None:
        """
        DESCR: Sets new coordinates for thos object
        """
        logger.debug(f"Object's {self} at {id(self)} attribute \"x\" changed: {self.x} -> {position_x}.")
        self.x = position_x
        logger.debug(f"Object's {self} at {id(self)} attribute \"x\" changed: {self.y} -> {position_y}.")
        self.y = position_y

        return None
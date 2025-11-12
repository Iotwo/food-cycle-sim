import logging

from classes.basic_object import BasicObject


logger = logging.getLogger(__name__)


class Ground(BasicObject):
    """
    DESCR: Class represents terrain field object
    """

    @BasicObject._general_logger
    def __init__(self, position_x: int, position_y: int, illumination: int=None, occupation: bool=None) -> None:
        logger.debug(f"Object {self} at {id(self)} calling ancestor's method \"{super(object, self).__init__.__name__}\".")
        super(Ground, self).__init__(position_x, position_y)
        
        self.INT_ILLUMINATION_VALUE_MAX = int(100)  # maximum possible value of illumination
        self.INT_ILLUMINATION_VALUE_MIN = int(0)  # minimum possible value of illumination
        self.INT_FERTILITY_VALUE_MAX = int(100)
        self.INT_FERTILITY_VALUE_MIN = int(0)
        
        self.illumination_value = illumination if illumination is not None else 0  # how much light energy can be stored in this block (Producenses)
        self.fertility_value = 0  # current value of food (i.e. corpse) left in this block (Reducenses)
        
        self.ground_type = 0

        self.is_occupied = occupation if occupation is not None else False

        self.speed_modifier = 0  # how does this block affects speed of the unit.
        
        self.tile = "G"

        logger.debug(f"Ground instance {self} at {id(self)} state after initialization: {vars(self)}.")

        return None

    def __new__(cls, *args, **kwargs) -> BasicObject:
        instance = super(Ground, cls).__new__(cls, *args, **kwargs)

        instance.INT_FERTILITY_VALUE_MAX = None
        instance.INT_FERTILITY_VALUE_MIN = None
        instance.fertility_value = None

        instance.INT_ILLUMINATION_VALUE_MAX = None
        instance.INT_ILLUMINATION_VALUE_MIN = None
        instance.illumination_value = None
        
        instance.ground_type = None

        instance.is_occupied = None

        instance.speed_modifier = None

        return instance


    @BasicObject._general_logger
    def _get_fertility_boundaries(self) -> tuple:
        """
        DESCR: Get current numerical boundaries for attribute "fertility value" of this block.
        """

        return (self.INT_FERTILITY_VALUE_MIN, self.INT_FERTILITY_VALUE_MAX,)

    @BasicObject._general_logger
    def _get_illumination_boundaries(self) -> tuple:
        """
        DESCR: Get current numerical boundaries for attribute "illumination value" of this block.
        """

        return (self.INT_ILLUMINATION_VALUE_MIN, self.INT_ILLUMINATION_VALUE_MAX,)

    @BasicObject._general_logger
    def get_fertility_value(self,) -> int:
        """
        DESCR: Get current fertility value for this block.
        """

        return self.fertility_value    

    @BasicObject._general_logger
    def get_ground_type(self,) -> int:
        """
        DESCR: Get ground type of this block.
        """

        return self.ground_type

    @BasicObject._general_logger
    def get_illumination(self,) -> int:
        """
        DESCR: Get current illumination value for this block.
        """

        return self.illumination_value

    @BasicObject._general_logger
    def get_occupation(self,) -> bool:
        """
        DESCR: Get current occupation value for this block.
        """

        return self.is_occupied;

    @BasicObject._general_logger
    def get_speed_modifier(self,) -> bool:
        """
        DESCR: Get current occupation value for this block.
        """

        return self.speed_modifier;

    @BasicObject._general_logger
    def set_fertility(self, fertility: int) -> None:
        """
        DESCR: Set new ground fertility value
        ARGS:
            - fertility: new value for block fertility, must be within boundaries
        """

        if fertility > self.INT_FERTILITY_VALUE_MAX:
            logger.info(f"Method \"Ground.set_fertility\" called with argument \"fertility\" higher than max bound: {fertility} > {self.INT_FERTILITY_VALUE_MAX}. Max value applied instead.")
        elif fertility < self.INT_FERTILITY_VALUE_MIN:
            logger.info(f"Method \"Ground.set_fertility\" called with argument \"fertility\" higher than max bound: {fertility} > {self.INT_FERTILITY_VALUE_MIN}. Max value applied instead.")
        else:
            pass
        logger.debug(f"Object's {self} at {id(self)} attribute \"fertility_value\" changed: {self.fertility_value} -> {fertility}.")
        self.fertility_value = fertility

        return None

    @BasicObject._general_logger
    def set_illumination(self, illumination: int) -> None:
        """
        DESCR: Set new ground illumination value
        ARGS:
            - illumination: new value for block illumination, must be within boundaries
        """

        if illumination > self.INT_ILLUMINATION_VALUE_MAX:
            logger.info(f"Method \"Ground.set_illumination\" called with argument \"illumination\" higher than max bound: {illumination} > {self.INT_ILLUMINATION_VALUE_MAX}. Max value applied instead.")
            illumination = self.INT_ILLUMINATION_VALUE_MAX
        elif illumination < self.INT_ILLUMINATION_VALUE_MIN:
            logger.info(f"Method \"Ground.set_illumination\" called with argument \"illumination\" lower than min bound: {illumination} > {self.INT_ILLUMINATION_VALUE_MIN}. Max value applied instead.")
            illumination = self.INT_ILLUMINATION_VALUE_MIN
        else:
            pass
        logger.debug(f"Object's {self} at {id(self)} attribute \"illumination_value\" changed: {self.illumination_value} -> {illumination}.")
        self.illumination_value = illumination

        return None

    @BasicObject._general_logger
    def set_occupation(self, occupation: bool) -> None:
        logger.debug(f"Object's {self} at {id(self)} attribute \"is_occupied\" changed: {self.is_occupied} -> {occupation}.")
        self.is_occupied = occupation;

        return None
import logging

from classes.basic_object import BasicObject


logger = logging.getLogger(__name__)


class UnitCorpse(BasicObject):
    """
    DESCR: This class represents corpse of any unit. Also it's basic class for all units
    """

    @BasicObject._general_logger
    def __init__(self, position_x: int, position_y: int) -> None:
        logger.debug(f"Object {self} at {id(self)} calling ancestor's method \"{super(object, self).__init__.__name__}\".")
        super(UnitCorpse, self).__init__(position_x, position_y)

        self.tile = 'T'

        return None

    def __new__(cls, *args, **kwargs) -> BasicObject:
        instance = super(UnitCorpse, cls).__new__(cls, *args, **kwargs)

        instance.INT_DAMAGE_VALUE_MIN = None
        instance.INT_DAMAGE_VALUE_MAX = None
        instance.INT_DAMAGE_VALUE_DEVIATION = None
        instance.damage_value = None

        instance.INT_MOVING_SPEED_MIN = None
        instance.INT_MOVING_SPEED_MAX = None
        instance.INT_MOVING_SPEED_DEVIATION = None
        instance.moving_speed = None

        instance.INT_HEALTH_VALUE_MIN = None
        instance.INT_HEALTH_VALUE_MAX = None
        instance.INT_HEALTH_VALUE_DEVIATION = None
        instance.health_value = None
        
        instance.INT_HUNGER_VALUE_MIN = None
        instance.INT_HUNGER_VALUE_MAX = None
        instance.INT_HUNGER_VALUE_DEVIATION = None
        instance.hunger_value = None

        instance.INT_SIGHT_VALUE_MIN = None
        instance.INT_SIGHT_VALUE_MAX = None
        instance.INT_SIGHT_VALUE_DEVIATION = None
        instance.sight_value = None

        instance.LIFE_STATES = None
        instance.life_state = None

        instance.generation = None
        instance.genome_set = None

        instance.instance_name = None
        
        instance.is_ready_to_reproduce = None

        return instance


    @BasicObject._general_logger
    def _calculate_genotype(self, phenotype: str=None) -> str:
        return self.genome_set

    @BasicObject._general_logger
    def _get_damage_boundaries(self,) -> tuple:
        """
        DESCR: Get damage value boundaries and deviation for this subclass.
        RETURN: tuple (min, max, available deviation)
        """

        return (self.INT_DAMAGE_VALUE_MIN, self.INT_DAMAGE_VALUE_MAX, self.INT_DAMAGE_VALUE_DEVIATION)

    @BasicObject._general_logger
    def _get_health_boundaries(self,) -> tuple:
        """
        DESCR: Get health value boundaries and deviation for this subclass.
        RETURN: tuple (min, max, available deviation)
        """

        return (self.INT_HEALTH_VALUE_MIN, self.INT_HEALTH_VALUE_MAX, self.INT_HEALTH_VALUE_DEVIATION)

    @BasicObject._general_logger
    def _get_hunger_boundaries(self,) -> tuple:
        """
        DESCR: Get hunger value boundaries and deviation for this subclass.
        RETURN: tuple (min, max, available deviation)
        """

        return (self.INT_HUNGER_VALUE_MIN, self.INT_HUNGER_VALUE_MAX, self.INT_HUNGER_VALUE_DEVIATION)

    @BasicObject._general_logger
    def _get_speed_boundaries(self,) -> tuple:
        """
        DESCR: Get speed value boundaries and deviation for this subclass.
        RETURN: tuple (min, max, available deviation)
        """

        return (self.INT_MOVING_SPEED_MIN, self.INT_MOVING_SPEED_MAX, self.INT_MOVING_SPEED_DEVIATION)

    @BasicObject._general_logger
    def _set_name(self, name: str) -> None:
        """
        DESCR: Set name for this instance to allow differentiation
        """
        logger.debug(f"Object's {self} at {id(self)} attribute \"instance_name\" changed: {self.instance_name} -> {name}.")
        self.instance_name = name

        return None


    @BasicObject._general_logger
    def check_reproduce_ready(self,) -> bool:
        """
        DESCR: check settings for procreate behaviour and switch inner value of readiness.
        RETURN: new value of is_ready_to_reproduce
        """
        return self.is_ready_to_reproduce

    @BasicObject._general_logger
    def get_damage_value(self,) -> int:
        return self.damage_value

    @BasicObject._general_logger
    def get_generation(self,) -> int:
        return self.generation

    @BasicObject._general_logger
    def get_moving_speed(self,) -> int:
        """
        DESCR: Get ground type of this block.
        """

        return self.moving_speed

    @BasicObject._general_logger
    def get_health_value(self,) -> int:
        """
        DESCR: Get ground type of this block.
        """

        return self.health_value

    @BasicObject._general_logger
    def get_hunger_value(self,) -> int:
        """
        DESCR: Get ground type of this block.
        """

        return self.hunger_value

    @BasicObject._general_logger
    def get_reproduce_switch(self) -> bool:
        return self.is_ready_to_reproduce

    @BasicObject._general_logger
    def consume(self,) -> None:
        """
        DESCR: Change this object hunger level, implementation depends on subtype
        ARGS:
        NOTE: Corpses cannot consume, this is a parent method for this class subtree
        NOTE: All checks must be implemented somewhere else
        """
        return None

    @BasicObject._general_logger
    def move(self, new_position: tuple) -> None:
        """
        DESCR: Change this object coordinates according to it's speed
        ARGS:
        NOTE: Corpses cannot move, this is a parent method for this class subtree
        NOTE: All checks must be implemented somewhere else
        """
        return None

    @BasicObject._general_logger
    def reproduce(self,) -> None:
        """
        DESCR: This method creates attributes for new exemplar of it's kind, creation of the new object lies on a high-level methods
        ARGS:
        NOTE: Corpses cannot reproduce, this is a parent method for this class subtree
        NOTE: All checks must be implemented somewhere else
        """
        return None

    @BasicObject._general_logger
    def set_damage(self, damage: int) -> None:
        """
        DESCR: Set new speed value for this exemplar
        """

        if speed > self.INT_DAMAGE_VALUE_MAX:
            logger.info(f"Method \"Ground.set_damage\" called with argument \"damage\" higher than max bound: {damage} > {self.INT_DAMAGE_VALUE_MAX}. Max value applied instead.")
            damage = self.INT_DAMAGE_VALUE_MAX
        elif speed < self.INT_DAMAGE_VALUE_MIN:
            logger.info(f"Method \"Ground.set_damage\" called with argument \"damage\" lower than min bound: {damage} < {self.INT_DAMAGE_VALUE_MIN}. Min value applied instead.")
            damage = self.INT_DAMAGE_VALUE_MIN
        else:
            pass
        logger.debug(f"Object's {self} at {id(self)} attribute \"damage\" changed: {self.damage_value} -> {damage}.")
        self.damage_value = damage

        return None

    @BasicObject._general_logger
    def set_moving_speed(self, speed: int) -> None:
        """
        DESCR: Set new speed value for this exemplar
        """

        if speed > self.INT_MOVING_SPEED_MAX:
            logger.info(f"Method \"Ground.set_moving_speed\" called with argument \"speed\" higher than max bound: {speed} > {self.INT_MOVING_SPEED_MAX}. Max value applied instead.")
            speed = self.INT_MOVING_SPEED_MAX
        elif speed < self.INT_MOVING_SPEED_MIN:
            logger.info(f"Method \"Ground.set_moving_speed\" called with argument \"speed\" lower than min bound: {speed} < {self.INT_MOVING_SPEED_MIN}. Min value applied instead.")
            speed = self.INT_MOVING_SPEED_MIN
        else:
            pass
        logger.debug(f"Object's {self} at {id(self)} attribute \"moving_speed\" changed: {self.moving_speed} -> {speed}.")
        self.moving_speed = speed

        return None

    @BasicObject._general_logger
    def set_health_value(self, health: int) -> None:
        """
        DESCR: Set new health value for this exemplar
        """

        if health > self.INT_HEALTH_VALUE_MAX:
            logger.info(f"Method \"Ground.set_health_value\" called with argument \"health\" higher than max bound: {health} > {self.INT_HEALTH_VALUE_MAX}. Max value applied instead.")
            health = self.INT_HEALTH_VALUE_MAX
        elif health < self.INT_HEALTH_VALUE_MIN:
            logger.info(f"Method \"Ground.set_health_value\" called with argument \"health\" lower than min bound: {health} < {self.INT_HEALTH_VALUE_MIN}. Min value applied instead.")
            health = self.INT_HEALTH_VALUE_MIN
        else:
            pass
        logger.debug(f"Object's {self} at {id(self)} attribute \"health_value\" changed: {self.health_value} -> {health}.")
        self.health_value = health

        return None

    @BasicObject._general_logger
    def set_hunger_value(self, hunger: int) -> None:
        """
        DESCR: Set new hunger value for this exemplar.
        """

        if hunger > self.INT_HUNGER_VALUE_MAX:
            logger.info(f"Method \"Ground.set_hunger_value\" called with argument \"hunger\" higher than max bound: {hunger} > {self.INT_HUNGER_VALUE_MAX}. Max value applied instead.")
            hunger = self.INT_HUNGER_VALUE_MAX
        elif hunger < self.INT_HUNGER_VALUE_MIN:
            logger.info(f"Method \"Ground.set_hunger_value\" called with argument \"hunger\" lower than min bound: {hunger} > {self.INT_HUNGER_VALUE_MIN}. Min value applied instead.")
            hunger = self.INT_HUNGER_VALUE_MIN
        else:
            pass
        logger.debug(f"Object's {self} at {id(self)} attribute \"hunger_value\" changed: {self.hunger_value} -> {hunger}.")
        self.hunger_value = hunger

        return None

    @BasicObject._general_logger
    def set_reproduce_switch(self, is_ready: bool) -> None:
        """
        DESCR:  Set new is_ready_to_reproduce value for this exemplar
        """
        logger.debug(f"Object's {self} at {id(self)} attribute \"is_ready_to_reproduce\" changed: {self.is_ready_to_reproduce} -> {is_ready}.")
        self.is_ready_to_reproduce = is_ready

        return None

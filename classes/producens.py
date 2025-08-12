import logging

from classes.unit_corpse import UnitCorpse
from classes.basic_object import BasicObject


logger = logging.getLogger(__name__)


class Producens(UnitCorpse):
    @BasicObject._general_logger
    def __init__(self, position_x: int, position_y: int, generation: int=0, phenotype: str="") -> None:
        logger.debug(f"Object {self} at {id(self)} calling ancestor's method \"{super(object, self).__init__.__name__}\".")
        super(Producens, self).__init__(position_x, position_y)

        self.INT_DAMAGE_VALUE_MIN = 0
        self.INT_DAMAGE_VALUE_MAX = 0
        self.INT_DAMAGE_VALUE_DEVIATION = None
        self.damage_value = 0

        self.INT_MOVING_SPEED_MIN = 0
        self.INT_MOVING_SPEED_MAX = 5
        self.INT_MOVING_SPEED_DEVIATION = None
        self.moving_speed = 1

        self.INT_HEALTH_VALUE_MIN = 0
        self.INT_HEALTH_VALUE_MAX = 10
        self.INT_HEALTH_VALUE_DEVIATION = None
        self.health_value = 10
        
        self.INT_HUNGER_VALUE_MIN = 0
        self.INT_HUNGER_VALUE_MAX = 10
        self.INT_HUNGER_VALUE_DEVIATION = None
        self.hunger_value = 0

        self.INT_SIGHT_VALUE_MIN = 1
        self.INT_SIGHT_VALUE_MAX = 10
        self.INT_SIGHT_VALUE_DEVIATION = None
        self.sight_value = 3

        self.LIFE_STATES = ("alive", "dead",)
        self.life_state = "alive"
        
        self.generation = generation
        self.genome_set = self._calculate_genotype(phenotype)

        self.instance_name = None
        
        self.is_ready_to_reproduce = False

        self.tile = 'P'

        logger.debug(f"BasicObject instance {self} at {id(self)} state after initialization: {vars(self)}.")

        return None

    def __new__(cls, *args, **kwargs) -> UnitCorpse:
        instance = super(Producens, cls).__new__(cls, *args, **kwargs)

        return instance
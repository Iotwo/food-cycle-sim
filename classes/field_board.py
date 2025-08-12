import logging

from classes.basic_object import BasicObject
from classes.ground import Ground
from classes.lighter import Lighter
from classes.unit_corpse import UnitCorpse


logger = logging.getLogger(__name__)


class FieldBoard(BasicObject):
    """
    DESCR: Package class for all model objects
    """
    @BasicObject._general_logger
    def __init__(self, size_x: int, size_y: int) -> None:
        logger.debug(f"Object {self} at {id(self)} calling ancestor's method \"{super(object, self).__init__.__name__}\".")
        super(FieldBoard, self).__init__(size_x, size_y)

        self.INT_MIN_SIDE_SIZE = 5  # minimum size of the field
        self.INT_FIELD_DIFF = 2  # difference between field size and populatable field size

        self.blocks_count = 0
        self.blocks_occupied = 0

        self.field = []
        self.creatures = []

        if self.x < self.INT_MIN_SIDE_SIZE:
            logger.info(f"{self} at {id(self)} was init with \"FieldBoard.x\" lower than allowed: {size_x} < {self.INT_MIN_SIDE_SIZE}. Min value applied instead.")
            self.x = self.INT_MIN_SIDE_SIZE  
        if self.y < self.INT_MIN_SIDE_SIZE:
            logger.info(f"{self} at {id(self)} was init with \"FieldBoard.y\" lower than allowed: {size_y} < {self.INT_MIN_SIDE_SIZE}. Min value applied instead.")
            self.y = self.INT_MIN_SIDE_SIZE  
        self.field_x = self.x - self.INT_FIELD_DIFF
        self.field_y = self.y - self.INT_FIELD_DIFF

        self.field = [[None for j in range(self.field_x)] for i in range(self.field_y)]

        logger.debug(f"FieldBoard instance {self} at {id(self)} state after initialization: {vars(self)}.")

        return None

    def __new__(cls, *args, **kwargs) -> BasicObject:
        instance = super(FieldBoard, cls).__new__(cls, *args, **kwargs)

        instance.blocks_count = None
        instance.blocks_occupied = None

        instance.creatures = None
        instance.field_x = None
        instance.field_y = None
        instance.field = None
        instance.lighter = None

        return instance

    @BasicObject._general_logger
    def _get_blocks_count(self,) -> int:
        return sum([1 if elem is not None else 0 for elem in line for line in self.field])

    @BasicObject._general_logger
    def _get_occupied_blocks_count(self,) -> int:
        count = 0

        for line in self.field:
            for elem in line:
                if elem is not None:
                    count = count + 1 if elem.get_occupation() is True else count

        return count

    @BasicObject._general_logger
    def _get_euclidean_distance_between_blocks(self, block_1: Ground, block_2: Ground) -> float:
        return 0.0

    @BasicObject._general_logger
    def _get_manhattan_distance_between_blocks(self, block_1: Ground, block_2: Ground) -> int:
        dist_x = abs(block_1.x - block_2.x)
        dist_y = abs(block_1.y - block_2.y)

        return dist_x + dist_y

    @BasicObject._general_logger
    def _get_rounded_euclidean_distance_between_block_and_lighter(self, block: Ground) -> int:
        """
        DESCR: Gets Euclid's distance between self.lighter and passed block from self.field
        ARGS:
            - block: exact ground segment of the field to which distance calculates to
        RETURN: integer rounded value as distance between self.lighter and block from self.field
        NOTE: direct calculation is not very effective
        """

        dist = int(((self.lighter.x - block.x) ** 2 + (self.lighter.y - block.y) ** 2) ** 0.5)

        return 0

    @BasicObject._general_logger
    def _get_manhattan_distance_between_block_and_lighter(self, block: Ground) -> int:
        """
        DESCR: Gets Manhattans distance between self.lighter and passed block from self.field
        ARGS:
            - block: exact ground segment of the field to which distance calculates to
        RETURN: integer value as distance between self.lighter and block from self.field
        """
        dist_x = abs(self.lighter.x - block.x)
        dist_y = abs(self.lighter.y - block.y)

        return dist_x + dist_y

    @BasicObject._general_logger
    def _calculate_light_radiation(self, distance: int) -> int:
        """
        DESCR: calculate lumination value of self.lighter at passed distance radius
        ARGS:
            - distance: radius at which illumination value need to be calculated
        RETURN: integer rounded value 
        """
        rad_value = self.lighter.power - distance
        if rad_value > 0:
            return rad_value
        
        return 0


    @BasicObject._general_logger
    def add_creature(self, creature: UnitCorpse) -> None:

        self.creatures.append(creature)
        logger.debug(f"{self} at {id(self)} added new creature {id(creature)} of type {type(creature)} to FieldBoard.creatures. Creatures total: {len(self.creatures)}")

        return None

    @BasicObject._general_logger
    def get_size(self,) -> tuple:
        """
        DESCR: Get exemplar size
        RETURN: tuple: size on X, size on Y
        """

        return (self.x, self.y)

    @BasicObject._general_logger
    def get_field_size(self,) -> tuple:
        """
        DESCR: Get size of model field
        RETURN: tuple: (size on X, size on Y)
        """

        return (self.field_x, self.field_y)

    @BasicObject._general_logger
    def redraw(self,) -> list:
        """
        DESCR: Draws pseudo graphical view of the field
        RETURN: list of lists containing lines of graphic interpretation
        NOTE: think about better solution
        """
        
        board = [['-' if self.field[y][x] is None else self.field[y][x].redraw() for x in range(self.field_x)] for y in range(self.field_y)]

        for creature in self.creatures:
            board[creature.y][creature.x] = creature.redraw()

        for y in range(self.field_y):
            board[y].insert(0, '-')
            board[y].append('-')

        board.insert(0, ['-' for _ in range(self.x)])
        board.append(['-' for _ in range(self.x)])

        board[self.lighter.y][self.lighter.x] = self.lighter.redraw()

        return board

    @BasicObject._general_logger
    def remove_creature(self, creature_id: int) -> None:
        if (creature_id < 0 or creature_id >= len(self.creatures)):
            logger.info(f"Method \"FieldBoard.remove_creature\" called with argument \"creature_id\" out of bounds: {creature_id}. Removing aborted.")
            return None

        banished = self.creatures.pop(creature_id)
        logger.debug(f"Creature {id(banished)} removed from collection \"FieldBoard.creatures\".")
        del(banished)

        return None

    @BasicObject._general_logger
    def set_illumination(self,) -> int:
        """
        DESCR: If FieldBoard.lighter exists calculate and illumination for all Ground exemplars in FieldBoard.field
        """
        blocks_recalculated = 0

        if self.lighter is None:
            logger.info(f"Method \"FieldBoard.set_illumination\" called when FieldBoard.lighter is None. Nothing to calculate")
        if self.field is None:
            logger.info(f"Method \"FieldBoard.set_illumination\" called when FieldBoard.field is None. Nothing to calculate")

        for i in range(self.field_y):
            for j in range(self.field_x):
                if self.field[i][j] is not None:
                    logger.debug(f"{self} at {id(self)}, changing value Ground.illumination for object {type(field[i][j])} on {id(field[i][j])}...")
                    dst = self._get_rounded_euclidean_distance_between_block_and_lighter(elem)
                    elem.set_illumination(self._calculate_light_radiation(dst))  
                    blocks_recalculated += 1
                else:
                    logger.debug(f"{self} at {id(self)} contains no element in FieldBoard.field on index {i};{j}.")


        return blocks_recalculated

    @BasicObject._general_logger
    def set_lighter(self, lighter: Lighter) -> None:
        """
        DESCR: set new Lighter object into lighter slot.
        """

        self.lighter = lighter
        logger.debug(f"Lighter {lighter} at {id(lighter)} has been set as board lighter with method FieldBoard.set_lighter.")
        return None

    @BasicObject._general_logger
    def set_lighter_position(self, new_x: int, new_y: int) -> None:
        """
        DESCR: Set new position for Lighter object in slot.
        """

        if (new_y == 0 and (0 <= new_x < self.x)):
            pass
        elif (new_y == self.y - 1 and (0 <= new_x < self.x)):
            pass
        elif (new_x == 0 and (0 <= new_y < self.y)):
            pass
        elif (new_x == self.x - 1 and (0 <= new_y < self.y)):
            pass
        else:
            logger.debug(f"Got incorrect coordinates for object FieldBoard.Lighter. Position remains unchanged.")
            return None

        logger.debug(f"{self} at {id(self)} changed object FieldBoard.Lighter at {id(self.lighter)} attributes:[{self.lighter.get_position()} -> {tuple([new_x, new_y])}].")
        self.lighter.set_position(new_x, new_y)

        return None
"""
The goal is to build simulator on basic components

"""

import argparse
import logging
import sys
import time
import tkinter



from classes.ground import Ground
from classes.field_board import FieldBoard
from classes.lighter import Lighter
from classes.producens import Producens
from classes.unit_corpse import UnitCorpse


logger = logging.getLogger(__name__)
dt_start = time.strftime("%Y%m%d-%H%M%S")
logging.basicConfig(filename=f"applog_{dt_start}.log", encoding="utf-8", level=logging.DEBUG, 
                    format="%(asctime)s:[%(levelname)s-%(levelno)s](module:%(module)s, file:%(filename)s, line:%(lineno)d, %(funcName)s) || %(message)s")


def _general_logger(method, *args, **kwargs):  # what type will it return?
    """
    DESCR: method used for debug purposses, does nothing but describes the execution
    """
    result = None
    line = ""
    def decoration(self, *args, **kwargs) -> None:
        global result
        global line

        line = "Object {obj} at {id} calling \"{mth}\" with args:{a}, and kwargs:{kw}." 
        line = line.format(obj=self, id=id(self), mth=method.__name__, a=args, kw=kwargs)
        #print(line)
        logger.debug(line)
        try:
            result = method(self, *args, **kwargs)
            line = "The result of {obj}.{mth} is: {r}."
            line = line.format(obj=id(self), mth=method.__name__, r=result)
            #print(line)
            logger.debug(line)
        except Exception as e:
            line = "Exception occured while executing {obj}.{mth}. " +\
                   "Cause: {ex_ca} ; Class: {ex_cl} ; Context: {ex_co} ; Args: {ex_ar} ; Trace: {ex_tr}. " +\
                   "None will be returned." 
            line = line.format(obj=id(self), mth=method.__name__, ex_ca=e.__cause__, ex_cl=e.__class__,
                              ex_co=e.__context__, ex_ar=e.args, ex_tr=e.with_traceback)
            #print(line)
            logger.error(line)
            result = None
        
        return result
    
    return decoration

@_general_logger
def gui_create_main_window(win_width: int, win_height: int, win_icon_path: str=None,) -> tkinter.Tk:
    """
    DESCR: Create main window of the application.
    """
    
    win_main = tkinter.Tk()

    win_main.geometry(f"{str(win_width)}x{str(win_height)}")
    win_main.resizable(False, False)
    
    win_main.title("APP NAME HERE!")
    win_main.iconbitmap(default=win_icon_path)

    logger.debug(f"Object {win_main} at {id(win_main)} created. State: {vars(win_main)}")
    
    return win_main

@_general_logger
def gui_draw_field(screen:tkinter.Tk, field_pictogram: list) -> None:
    """
    DESCR: Draws field in tk widget according to passed pictogram
    ARGS:
        - screen: Tkinter window
        - field_pictogram: list of lists representing model objects placement
    """
    return None



@_general_logger
def eng_create_field(field_x: int, field_y: int, lighter_power: int, terrain_pattern: list=None) -> FieldBoard:
    """
    DESCR: Create field board of exact size and populate it with blocks of terrain
    ARGS:
        - field_x: horizontal field size
        - field_y: vertical field size
        - lighter_power: attached to field lighter's power
    RETURN: exemplar of class FieldBoard, with initiated field and lighter
    """

    logger.debug(f"Creating field {field_x}X{field_y}")
    instance = FieldBoard(field_x, field_y)

    logger.debug(f"Adding lighter with power {lighter_power}.")
    instance.set_lighter(Lighter(0, 0, lighter_power))

    return instance

@_general_logger
def eng_move_lighter_on_field(field: FieldBoard, moving_pattern: list) -> None:
    """
    DESCR: Method changes coordinates of object Lighter, imnitating it's movement around the field
    ARGS:
        - field: FieldBoard object with lighter within it.
        - moving_pattern: Path of the lighter
    """

    lighter_pos = field.lighter.get_position()
    for move in moving_pattern:
        if lighter_pos == move:
            logger.debug(f"Current coordinates of FieldBoard.Lighter at {id(field.lighter)} are {field.lighter.get_position()}, and matched with {moving_pattern.index(move)}'th fragment of moving pattern at {id(moving_pattern)}.")
            ligter_new_pos = (moving_pattern.index(move) + 1) % len(moving_pattern)
            logger.debug(f"New index of fragment from moving pattern at {id(moving_pattern)} is {ligter_new_pos}")
            field.lighter.set_position(moving_pattern[ligter_new_pos][0], moving_pattern[ligter_new_pos][1])
            logger.debug(f"New set of coordinates for FieldBoard.Lighter at {id(field.lighter)} is: {moving_pattern[ligter_new_pos]}")
            break

    return None


@_general_logger
def eng_check_coordinates_withtin_field(position: tuple, field: FieldBoard) -> bool:
    """
    DESCR: check that given coordinates are within given boundaries
    ARGS:
        - position: tuple of two coordinates, x and y
        - field: FieldBoard object with coordinate collection within.
    """

    result = True

    if position[1] < 0 or position[1] >= len(field.field):
        logger.info(f"Passed value of Y, {position[1]}, is out of bounds [0, {len(field.field)}].")
        result = False
    elif position[0] < 0 or position[0] >= len(field.field[position[1]]):
        logger.info(f"Passed value of X, {position[1]}, is out of bounds [0, {len(field.field[position[1]])}.")
        result = False
    else:
        pass

    return result

@_general_logger
def eng_check_choosen_object_is_a_cell(position: tuple, field: FieldBoard) -> bool:
    """
    """

    result = True
    
    if instance(field.field[position[1]][position[0]], Ground) is False:
        logger.info(f"Object at that position is not a Ground class or subclass.")
        result = False

    return result

@_general_logger
def eng_check_field_cell_not_occupied(position: tuple, field: FieldBoard) -> bool:
    """
    DESCR: Checks if target cell attribute is_occupied
    ARGS:
        - cell_pos: cell position (x, y)
        - field: FieldBoard used in model
    RETURN: True - if is_occupied is False, False otherwise
    """

    result = True

    if field.field[position[1]][position[0]] is None:
        logger.info(f"Given position, ({position[0]},{position[1]}) is None")
        return False
    result = not field.field[cell_pos[1]][cell_pos[0]].is_occupied
    
    return result

@_general_logger
def eng_fill_field(field: FieldBoard, pattern: list=None) -> int:
    """
    DESCR: fills FieldBoard exemplar with ground blocks
    ARGS:
        - field: FieldBoard exemplar to be filled, 
                 it is a link-type so will be changed anyway
        - pattern: fill field with custom ground blocks
    RETURN: count of spawned blocks
    NOTE: pattern usage not implemented yet
    """
    blocks_count = 0

    if pattern is not None:
        pass
    else:
        for y in range(field.field_y):
            for x in range(field.field_x):
                field.field[y][x] = Ground(x, y)
                blocks_count += 1

    return blocks_count

@_general_logger
def eng_get_unit_view(field: FieldBoard, unit: UnitCorpse) -> list:
    """
    DESCR: Get subselection of field to represent unit point of view
    """
    return []

@_general_logger
def eng_move_unit_on_field() -> None:
    return None

@_general_logger
def eng_populate_field(field: FieldBoard, creatures: list=None) -> None:

    if creatures is None:
        creatures = [
            Producens(0, 0),
        ]

    for unit in creatures:
        field.add_creature(unit)

    return None


if __name__ == '__main__':
    logger.info(f"Application started.")
    logger.debug(f"Passed arguments: [{sys.argv}]")

    TUPLE_LIGHTER_PATH = ((0, 0,),(0, 1,),(0, 2,),(0, 3,),(0, 4,),
                          (1, 4,),(2, 4,),(3, 4,),(4, 4,),
                          (4, 3,),(4, 2,),(4, 1,),(4, 0,),
                          (3, 0,),(2, 0,),(1, 0,),)
    STR_EXIT_SIGNAL = 'e'
    last_signal = ''

    # LOAD PREDEFINED DATA IF NOTHING PASSED
    #
    # PREPARE
    field = eng_create_field(5, 5, 3)
    eng_fill_field(field)
    # populate field

    # CYCLE
    #main = gui_create_main_window(640, 480)
    #main.mainloop()
    while last_signal.lower() != STR_EXIT_SIGNAL:
        print('cycle')
        eng_move_lighter_on_field(field, TUPLE_LIGHTER_PATH)
        # move creatures
        # act creatures
        print(field.redraw())
        last_signal = input('signal:')
        print("signal", last_signal)

    
    logger.info(f"Simulation finished. Cleaning up.")
    # CLEAN UP AND LEAVE

sys.exit(0)
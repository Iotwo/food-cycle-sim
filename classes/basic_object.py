import logging


logger = logging.getLogger(__name__)


class BasicObject(object):
    """
    DESCR: Basic class for all objects in model.
    """

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
    def __del__(self) -> None:
        logger.debug(f"Object {self} at {id(self)} state before deletion: {vars(self)}.")
        return None

    @_general_logger
    def __init__(self, position_x: int, position_y: int) -> None:
        logger.debug(f"Object {self} at {id(self)} calling ancestor's method \"{super(object, self).__init__.__name__}\"")
        super(BasicObject, self).__init__()
        self.x = position_x
        self.y = position_y

        return None

    @_general_logger
    def __new__(cls, *args, **kwargs) -> object:
        instance = super(BasicObject, cls).__new__(cls)

        instance.x = None
        instance.y = None
        
        instance.tile = None

        return instance


    @_general_logger
    def redraw(self,) -> str:
        """
        DESCR: Draw tile or call drawing graphical method. 
        """
        
        return self.tile
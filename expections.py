import Exception

class DataException(Exception):
    """Data Error

    """
    pass

class StructException(Exception):
    """
    """
    pass

class NeuronDataExpection(DataException):
    """The NeuronNet Data Error

    """
    pass

class InputDataExpection(DataException):
    """The Input Data Error

    """
    pass

class NeuronNerStructException(StructException):
    """
    """
    pass

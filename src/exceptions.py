# Custom Exceptions
class ETLException(Exception):
    pass

class ExtractionException(ETLException):
    pass

class TransformationException(ETLException):
    pass

class LoadingException(ETLException):
    pass
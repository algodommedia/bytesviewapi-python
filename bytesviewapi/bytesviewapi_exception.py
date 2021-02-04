class BytesviewException(Exception):
    """Represents an ''error'' response status value from News API."""

    def __init__(self, exception):
        self.exception = exception

    def get_exception(self):
        return self.exception
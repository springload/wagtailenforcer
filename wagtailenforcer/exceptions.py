
class WagtailenforcerException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(WagtailenforcerException, self).__init__(message)


class EnforcerVirusException(WagtailenforcerException):
    pass
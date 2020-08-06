class ConfigurationSettings:
    """
    Gets configuration settings
    """

    def __init__(self):
        self._connection_string = ""  # TODO: Add connection string

    @property
    def connection_string(self):
        return self._connection_string

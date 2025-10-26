class CommandingOfficer:
    """
    Oversees mission execution and strategic decisions.
    Interfaces with XO and sets global mission parameters.
    """

    def __init__(self):
        self.mission_config = {}

    def set_mission_config(self, config):
        self.mission_config = config

    def brief_xo(self, xo):
        xo.config = self.mission_config

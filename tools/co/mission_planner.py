class MissionPlanner:
    """Sets global mission parameters and strategic goals."""

    def __init__(self):
        self.config = {}

    def set_config(self, config):
        self.config = config

    def report(self):
        return self.config

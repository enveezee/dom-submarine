class ExecutiveOfficer:
    """
    Coordinates crew modules and enforces mission config.
    Acts as the bridge between CO and crew.
    """

    def __init__(self, config=None):
        self.config = config or {}
        self.log = []

    def issue_directive(self, officer, directive):
        officer.update_config(directive)
        self.log.append((officer.__class__.__name__, directive))

    def report(self):
        return self.log

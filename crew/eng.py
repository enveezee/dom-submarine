class EngineeringOfficer:
    """
    Manages system health, performance, and error recovery.
    Tracks tool failures and runtime diagnostics.
    """

    def __init__(self):
        self.diagnostics = []

    def log_issue(self, tool, error):
        self.diagnostics.append((tool, str(error)))

    def report(self):
        return self.diagnostics

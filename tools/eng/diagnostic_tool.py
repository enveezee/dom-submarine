class DiagnosticTool:
    """Logs system health, errors, and tool failures."""

    def __init__(self):
        self.issues = []

    def log(self, tool, error):
        self.issues.append((tool, str(error)))

    def report(self):
        return self.issues

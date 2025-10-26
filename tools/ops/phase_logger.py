class PhaseLogger:
    """Logs operational phases and mission checkpoints."""

    def __init__(self):
        self.checkpoints = []

    def mark(self, phase):
        self.checkpoints.append(phase)

    def report(self):
        return self.checkpoints

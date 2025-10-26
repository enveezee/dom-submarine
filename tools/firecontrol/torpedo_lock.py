class TorpedoLock:
    """Locks onto highest scoring nodes for extraction."""

    def __init__(self):
        self.locked_targets = []

    def lock(self, scores, threshold=5):
        self.locked_targets = [
            node_id for node_id, score in scores.items() if score >= threshold
        ]
        return self.locked_targets

    def report(self):
        return self.locked_targets

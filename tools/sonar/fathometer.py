class Fathometer:
    """Tracks tag depth and nesting structure for DOM traversal."""

    def __init__(self):
        self.depth = 0
        self.depth_map = []

    def descend(self, tag):
        self.depth += 1
        self.depth_map.append((tag, self.depth))

    def ascend(self):
        self.depth = max(0, self.depth - 1)

    def report(self):
        return self.depth_map

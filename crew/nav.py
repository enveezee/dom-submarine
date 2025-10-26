class Navigator:
    """
    Tracks DOM traversal path and coordinates tag depth.
    May interface with SonarTechnician and HullTech.
    """

    def __init__(self):
        self.path = []

    def enter(self, tag):
        self.path.append(tag)

    def exit(self):
        if self.path:
            self.path.pop()

    def report(self):
        return self.path

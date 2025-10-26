class SemanticScanner:
    """Scans for semantic zones and logs their attributes."""

    SEMANTIC_TAGS = {"main", "article", "section", "nav", "aside"}

    def __init__(self):
        self.zones = []

    def scan(self, tag, attrs):
        if tag in self.SEMANTIC_TAGS:
            self.zones.append({"tag": tag, "attrs": dict(attrs)})

    def report(self):
        return self.zones
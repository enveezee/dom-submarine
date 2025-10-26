class SVGStripper:
    """Strips SVG and vector graphics from the DOM."""

    def __init__(self):
        self.stripped = []

    def strip(self, node_id, tag):
        if tag == "svg":
            self.stripped.append(node_id)
            return True
        return False

    def report(self):
        return self.stripped

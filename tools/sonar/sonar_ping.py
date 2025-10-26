class SonarPing:
    """Logs echo returns from semantic hits and tag encounters."""

    def __init__(self):
        self.echo_log = []

    def ping(self, tag, depth, semantic_hit=False):
        self.echo_log.append({
            "tag": tag,
            "depth": depth,
            "semantic": semantic_hit
        })

    def report(self):
        return self.echo_log

class DirectiveDispatcher:
    """Issues directives to officers and tracks config changes."""

    def __init__(self):
        self.log = []

    def dispatch(self, officer, directive):
        officer.update_config(directive)
        self.log.append((officer.__class__.__name__, directive))

    def report(self):
        return self.log

class BufferTool:
    """
    Manages a rolling buffer of DOM nodes.
    Supports flush triggers and peek operations.
    """

    def __init__(self, max_size=100, flush_rules=None):
        self.buffer = []
        self.max_size = max_size
        self.flush_rules = flush_rules or []
        self.log = {"flushed": [], "peeked": []}

    def push(self, tag, attrs, data=None):
        self.buffer.append({
            'tag': tag,
            'attrs': dict(attrs),
            'data': data
        })
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)

    def flush(self):
        flushed = self.buffer[:]
        self.buffer.clear()
        self.log["flushed"].append(flushed)
        return flushed

    def peek(self, depth=5):
        peeked = self.buffer[-depth:]
        self.log["peeked"].append(peeked)
        return peeked

    def is_flush_trigger(self, tag, data):
        for rule in self.flush_rules:
            if rule["tag"] == tag and rule["match"] in (data or ""):
                return True
        return False

    def report(self):
        return self.log

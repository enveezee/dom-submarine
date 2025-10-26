from tools.cob.buffer_tool import BufferTool

class ChiefOfBuffer:
    """
    Officer responsible for managing DOM buffers.
    Coordinates BufferTool and responds to flush directives.
    """

    def __init__(self, config=None):
        self.config = config or {
            "max_size": 100,
            "flush_rules": [
                {"tag": "div", "match": "message"},
                {"tag": "section", "match": "payload"}
            ]
        }
        self.buffer_tool = BufferTool(
            max_size=self.config["max_size"],
            flush_rules=self.config["flush_rules"]
        )

    def receive(self, tag, attrs, data=None):
        self.buffer_tool.push(tag, attrs, data)
        if self.buffer_tool.is_flush_trigger(tag, data):
            return self.buffer_tool.flush()
        return None

    def peek(self, depth=5):
        return self.buffer_tool.peek(depth)

    def report(self):
        return self.buffer_tool.report()


class BufferManager:
    def __init__(self, max_size=100):
        self.buffer = []
        self.max_size = max_size

    def push(self, tag, attrs, data=None):
        """Add a new tag or data node to the buffer."""
        self.buffer.append({
            'tag': tag,
            'attrs': dict(attrs),
            'data': data
        })
        if len(self.buffer) > self.max_size:
            self.buffer.pop(0)

    def flush(self):
        """Flush the buffer and return its contents."""
        flushed = self.buffer[:]
        self.buffer.clear()
        return flushed

    def peek(self, depth=5):
        """Peek at the last N items in the buffer."""
        return self.buffer[-depth:]

    def is_flush_trigger(self, tag, data):
        """Determine if this tag/data signals a flush."""
        # Example: flush on closing a <div> with class 'message'
        if tag == 'div' and data and 'message' in data:
            return True
        return False

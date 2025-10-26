class NoiseFilter:
    """Removes known noise elements from the DOM."""

    NOISE_TAGS = {"script", "style", "noscript", "iframe"}
    NOISE_CLASSES = {"ad", "ads", "sponsored", "tracking", "cookie-banner"}

    def __init__(self):
        self.removed = []

    def is_noise(self, tag, attrs):
        if tag in self.NOISE_TAGS:
            return True
        for attr, val in attrs:
            if attr == "class":
                classes = val.split()
                if any(cls.lower() in self.NOISE_CLASSES for cls in classes):
                    return True
        return False

    def filter(self, node_id, tag, attrs):
        if self.is_noise(tag, attrs):
            self.removed.append(node_id)
            return True
        return False

    def report(self):
        return self.removed

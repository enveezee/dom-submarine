class ClassDegreaser:
    """Cleans and normalizes class attributes."""

    def __init__(self):
        self.cleaned = {}

    def degrease(self, node_id, attrs):
        new_attrs = []
        for attr, val in attrs:
            if attr == "class":
                classes = val.split()
                filtered = [cls for cls in classes if not cls.startswith("js-") and "track" not in cls]
                new_attrs.append((attr, " ".join(filtered)))
            else:
                new_attrs.append((attr, val))
        self.cleaned[node_id] = dict(new_attrs)
        return new_attrs

    def report(self):
        return self.cleaned

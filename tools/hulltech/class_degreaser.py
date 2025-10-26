class ClassDegreaser:
    """
    Degreases class attributes based on mission config.
    Preserves high-value selectors and logs decisions.
    """

    def __init__(self, config=None):
        self.config = config or {
            "preserve_test_hooks": True,
            "preserve_aria": True,
            "aggressive": False,
            "log_removed": True
        }
        self.cleaned = {}
        self.removed = {}

    def update_config(self, new_config):
        self.config.update(new_config)

    def degrease(self, node_id, attrs):
        new_attrs = []
        removed_classes = []

        for attr, val in attrs:
            if attr == "class":
                classes = val.split()
                filtered = []
                for cls in classes:
                    if self.config["aggressive"] and len(cls) <= 3:
                        removed_classes.append(cls)
                        continue
                    if cls.startswith("js-") or "track" in cls or "ad" in cls:
                        removed_classes.append(cls)
                        continue
                    if self.config["preserve_test_hooks"] and any(
                        hook in cls for hook in ["test", "qa", "data"]
                    ):
                        filtered.append(cls)
                        continue
                    filtered.append(cls)

                new_attrs.append((attr, " ".join(filtered)))
            elif attr.startswith("aria-") and self.config["preserve_aria"]:
                new_attrs.append((attr, val))
            else:
                new_attrs.append((attr, val))

        self.cleaned[node_id] = dict(new_attrs)
        if self.config["log_removed"] and removed_classes:
            self.removed[node_id] = removed_classes

        return new_attrs

    def report(self):
        return {
            "cleaned": self.cleaned,
            "removed": self.removed
        }

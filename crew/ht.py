from tools.hulltech.noise_filter import NoiseFilter
from tools.hulltech.svg_stripper import SVGStripper
from tools.hulltech.class_degreaser import ClassDegreaser

class HullTech:
    """
    Officer responsible for DOM sanitation:
    - NoiseFilter: Removes known noise elements
    - SVGStripper: Strips vector graphics
    - ClassDegreaser: Cleans bloated class attributes
    """

    def __init__(self, config=None):
        self.noise_filter = NoiseFilter()
        self.svg_stripper = SVGStripper()
        self.class_degreaser = ClassDegreaser()
        self.config = config or {
            "strip_svg": True,
            "filter_noise": True,
            "degrease_classes": True,
            "preserve_test_hooks": True,
            "aggressive_mode": False
        }
        self.log = {
            "removed": [],
            "preserved": [],
            "cleaned": {}
        }

    def update_config(self, new_config):
        self.config.update(new_config)

    def sanitize(self, node_id, tag, attrs):
        """Run sanitation tools based on current config."""
        if self.config["filter_noise"] and self.noise_filter.filter(node_id, tag, attrs):
            self.log["removed"].append((node_id, "noise"))
            return None

        if self.config["strip_svg"] and self.svg_stripper.strip(node_id, tag):
            self.log["removed"].append((node_id, "svg"))
            return None

        cleaned_attrs = attrs
        if self.config["degrease_classes"]:
            cleaned_attrs = self.class_degreaser.degrease(node_id, attrs)
            self.log["cleaned"][node_id] = cleaned_attrs

        return cleaned_attrs

    def report(self):
        return self.log

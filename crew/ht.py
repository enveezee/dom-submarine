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

    def __init__(self):
        self.noise_filter = NoiseFilter()
        self.svg_stripper = SVGStripper()
        self.class_degreaser = ClassDegreaser()

    def sanitize(self, node_id, tag, attrs):
        """Run all sanitation tools on a node. Returns cleaned attrs or None if node should be removed."""
        if self.noise_filter.filter(node_id, tag, attrs):
            return None
        if self.svg_stripper.strip(node_id, tag):
            return None
        cleaned_attrs = self.class_degreaser.degrease(node_id, attrs)
        return cleaned_attrs

    def report(self):
        """Returns full hull maintenance report."""
        return {
            "removed_noise": self.noise_filter.report(),
            "stripped_svg": self.svg_stripper.report(),
            "cleaned_classes": self.class_degreaser.report()
        }

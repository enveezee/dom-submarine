from tools.sonar.fathometer import Fathometer
from tools.sonar.semantic_scanner import SemanticScanner
from tools.sonar.sonar_ping import SonarPing

class SonarTechnician:
    """
    Officer responsible for managing sonar tools:
    - Fathometer: Tracks tag depth
    - SemanticScanner: Detects semantic zones
    - SonarPing: Logs echo returns
    """

    def __init__(self):
        self.fathometer = Fathometer()
        self.scanner = SemanticScanner()
        self.ping_log = SonarPing()

    def enter_tag(self, tag, attrs):
        """Called when entering a tag."""
        self.fathometer.descend(tag)
        self.scanner.scan(tag, attrs)
        self.ping_log.ping(
            tag=tag,
            depth=self.fathometer.depth,
            semantic_hit=(tag in self.scanner.SEMANTIC_TAGS)
        )

    def exit_tag(self):
        """Called when exiting a tag."""
        self.fathometer.ascend()

    def report(self):
        """Returns a full sonar report."""
        return {
            "depth_map": self.fathometer.report(),
            "semantic_zones": self.scanner.report(),
            "echo_log": self.ping_log.report()
        }


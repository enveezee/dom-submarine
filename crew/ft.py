from tools.firecontrol.strike_protocol import StrikeProtocol
from tools.firecontrol.targeting_system import TargetingSystem
from tools.firecontrol.torpedo_lock import TorpedoLock

class FireControlOfficer:
    """
    Officer responsible for identifying and striking semantic targets:
    - TargetingSystem: Scores nodes based on relevance
    - TorpedoLock: Locks onto high-value targets
    - StrikeProtocol: Prepares payload for extraction
    """

    def __init__(self):
        self.targeting = TargetingSystem()
        self.lock = TorpedoLock()
        self.strike = StrikeProtocol()

    def evaluate_node(self, node_id, tag, attrs, depth):
        """Score a node during traversal."""
        return self.targeting.score_node(node_id, tag, attrs, depth)

    def lock_targets(self, threshold=5):
        """Lock onto high-value targets."""
        scores = self.targeting.report()
        return self.lock.lock(scores, threshold)

    def prepare_payload(self, dom_map):
        """Prepare extraction payload from locked targets."""
        locked = self.lock.report()
        self.strike.prepare(dom_map, locked)
        return self.strike.report()

    def report(self):
        """Returns full fire control report."""
        return {
            "scores": self.targeting.report(),
            "locked_targets": self.lock.report(),
            "payload": self.strike.report()
        }

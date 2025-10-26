from crew.sts import SonarTechnician
from crew.ft import FireControlOfficer
from crew.ht import HullTech
from crew.cob import ChiefOfBuffer
from crew.xo import ExecutiveOfficer
from crew.co import CommandingOfficer
from crew.nav import Navigator
from crew.eng import EngineeringOfficer
from crew.intel import IntelligenceOfficer
from crew.ops import OperationsOfficer

class Submarine:
    """
    Central vessel coordinating crew modules and mission execution.
    """

    def __init__(self, config=None):
        self.config = config or {}

        # Officers
        self.co = CommandingOfficer()
        self.xo = ExecutiveOfficer(config=self.config)
        self.sts = SonarTechnician()
        self.ft = FireControlOfficer()
        self.ht = HullTech(config=self.config.get("hulltech"))
        self.cob = ChiefOfBuffer(config=self.config.get("buffer"))
        self.nav = Navigator()
        self.eng = EngineeringOfficer()
        self.intel = IntelligenceOfficer()
        self.ops = OperationsOfficer()

        # Mission state
        self.dom_map = {}
        self.payload = []

    def deploy(self, dom):
        """
        Entry point for DOM traversal and crew coordination.
        Stubbed for now.
        """
        # TODO: Traverse DOM, coordinate officers, extract payload
        pass

    def report(self):
        """
        Returns full mission report from all officers.
        """
        return {
            "sonar": self.sts.report(),
            "fire_control": self.ft.report(),
            "hull_tech": self.ht.report(),
            "buffer": self.cob.report(),
            "executive": self.xo.report(),
            "command": self.co.mission_config,
            "navigation": self.nav.report(),
            "engineering": self.eng.report(),
            "intel": self.intel.report(),
            "operations": self.ops.report(),
            "payload": self.payload
        }

class StrikeProtocol:
    """Prepares locked nodes for extraction and formats payload."""

    def __init__(self):
        self.payload = []

    def prepare(self, dom_map, locked_targets):
        for node_id in locked_targets:
            if node_id in dom_map:
                node = dom_map[node_id]
                self.payload.append({
                    "id": node_id,
                    "tag": node["tag"],
                    "text": node.get("text", ""),
                    "attrs": node.get("attrs", {})
                })

    def report(self):
        return self.payload

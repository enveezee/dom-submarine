class TargetingSystem:
    """Scores DOM nodes based on semantic weight and relevance."""

    def __init__(self):
        self.scores = {}

    def score_node(self, node_id, tag, attrs, depth):
        score = 0

        # Tag-based scoring
        if tag in {"h1", "h2", "article", "main"}:
            score += 5
        elif tag in {"p", "section", "div"}:
            score += 2

        # Attribute-based scoring
        for attr, val in attrs:
            if "content" in val or "main" in val:
                score += 3
            if "header" in val or "title" in val:
                score += 4

        # Depth penalty (deeper = less likely to be primary)
        score -= depth * 0.5

        self.scores[node_id] = score
        return score

    def report(self):
        return self.scores
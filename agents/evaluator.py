
class EvaluatorAgent:
    def __init__(self):
        pass

    def evaluate(self, result):
        if "risks" in result and result["risks"]:
            return "Risks successfully identified."
        return "No significant risks found."

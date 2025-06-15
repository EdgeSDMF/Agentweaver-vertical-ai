
class PlannerAgent:
    def __init__(self, goal):
        self.goal = goal

    def plan(self):
        return [
            "Retrieve patient context",
            "Summarize EHR and extract risks",
            "Evaluate response"
        ]

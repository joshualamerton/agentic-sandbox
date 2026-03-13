class Scenario:

    def __init__(self, description, goal):
        self.description = description
        self.goal = goal

    def initial_state(self):
        return {
            "task": self.goal,
            "completed": False
        }

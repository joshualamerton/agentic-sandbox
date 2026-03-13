class Sandbox:

    def __init__(self, agent, scenario):
        self.agent = agent
        self.state = scenario.initial_state()

    def step(self):
        action = self.agent.decide(self.state)

        if action == "complete_task":
            self.state["completed"] = True

        return self.state

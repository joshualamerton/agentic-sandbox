from core.agent_interface import AgentInterface
from core.sandbox import Sandbox
from core.scenario import Scenario
from core.evaluator import Evaluator


class SimpleAgent(AgentInterface):

    def decide(self, state):
        if not state["completed"]:
            return "complete_task"
        return "idle"


def main():

    scenario = Scenario(
        description="Complete a simple task",
        goal="finish_task"
    )

    agent = SimpleAgent("test_agent")

    sandbox = Sandbox(agent, scenario)
    evaluator = Evaluator()

    state = sandbox.step()

    result = evaluator.evaluate(state)

    print("Final state:", state)
    print("Evaluation:", result)


if __name__ == "__main__":
    main()

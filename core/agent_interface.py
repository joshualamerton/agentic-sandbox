class AgentInterface:

    def __init__(self, name):
        self.name = name

    def decide(self, state):
        """
        Agent receives environment state and returns an action.
        """
        raise NotImplementedError

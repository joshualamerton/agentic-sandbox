class Evaluator:

    def evaluate(self, state):
        if state["completed"]:
            return {"success": True}
        return {"success": False}

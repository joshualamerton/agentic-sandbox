# AgentSandbox Architecture

AgentSandbox is designed as a testing harness for autonomous agents.

The system consists of four primary components.

Agent Interface  
Defines how an agent interacts with the sandbox environment.

Sandbox Environment  
Controls the simulation and mediates interactions.

Scenario  
Defines the task, rules, and available tools.

Evaluation Engine  
Measures whether the agent successfully completes the objective.

Execution flow

1. Load a scenario
2. Initialize an agent
3. Provide the agent with environment state
4. Agent chooses an action
5. Sandbox executes the action
6. Evaluator scores the outcome

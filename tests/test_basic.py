from core.scenario import Scenario


def test_scenario_initial_state():
    scenario = Scenario("test", "goal")
    state = scenario.initial_state()
    assert state["completed"] is False

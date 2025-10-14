from example_1 import run_threads

def test_race_condition_fixed():
    result = run_threads()
    assert result == 20000, f"Expected 20000, got {result}"

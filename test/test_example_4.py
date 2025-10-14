from example_4 import run_lock_bugs

def test_lock_fixed():
    result = run_lock_bugs()
    assert result == 5, f"Expected 5, got {result}"

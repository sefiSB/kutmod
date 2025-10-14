from example_5 import run_safe

def test_no_change_needed():
    result = run_safe()
    assert result == 20000, f"Expected 20000, got {result}"

from example_4 import run_lock_bugs

def test_lock_bugs_fixed():
    value, still_running = run_lock_bugs()
    # Jó megoldás esetén value == 9 (3*(1+2)) és nincs futó szál
    assert value == 9, f"Expected 9, got {value}"
    assert not still_running, "Some threads did not finish – possible deadlock or leak"

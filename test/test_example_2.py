from example_2 import run_deadlock_and_race

def test_deadlock_and_race_fixed():
    finished, length = run_deadlock_and_race()
    # akkor jó, ha nincs deadlock és pontosan 5 elem került be (2+3)
    assert finished, "Threads did not finish – likely deadlock"
    assert length == 5, f"Expected 5 elements, got {length}"

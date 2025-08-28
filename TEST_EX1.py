
import EX1


def test_do_while_simulation():
    assert EX1.do_while_simulation() == [
        "Count is 0",
        "Count is 1",
        "Count is 2"
    ]


def test_while_do():
    assert EX1.while_do() == [
        "Count is 0",
        "Count is 1",
        "Count is 2"
    ]


def test_check_even_odd():
    assert EX1.check_even_odd(5) == "5 is odd"
    assert EX1.check_even_odd(10) == "10 is even"


def test_switch():
    assert EX1.switch(1) == "One"
    assert EX1.switch(2) == "Two"
    assert EX1.switch(3) == "Three"
    assert EX1.switch(89) == "Other"


def test_for_loop():
    assert EX1.for_loop() == [
        "Iteration 0",
        "Iteration 1",
        "Iteration 2"
    ]

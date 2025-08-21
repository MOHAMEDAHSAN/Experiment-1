# Experiment-1

### NAME : S MOHAMED AHSAN
### REG NO : 212223240089

##  Write programs in Python Language to demonstrate the working of
followingconstructs with possible test cases: a) do…while b) while…do c)
if …else d) switch e) for

## a) Aim
To write python programs for do…while, while, for, switch and if…else and test with possible test
cases.

## Algorithm
1.	Start the program.
2. Create separate files for each given program.
3. Write simple program for each construct.
4. Test the program with possible test cases.
5. Stop the program. 

## Program
### EX1.py
```python


# a) do...while simulation
def do_while_simulation():
    count = 0
    result = []
    while True:
        result.append(f"Count is {count}")
        count += 1
        if count >= 3:
            break
    return result


# b) while...do (standard while loop)
def while_do():
    count = 0
    result = []
    while count < 3:
        result.append(f"Count is {count}")
        count += 1
    return result


# c) if...else
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"


# d) switch case using match-case
def switch(value):
    match value:
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case _:
            return "Other"


# e) for loop
def for_loop():
    return [f"Iteration {i}" for i in range(3)]
```
### TEST_EX1.py
```python

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

```
## Output
<img width="1215" height="349" alt="image" src="https://github.com/user-attachments/assets/9fe7ace9-ae92-40e7-8103-b1846874d096" />

## Result  
All the Python constructs (do…while, while, if…else, switch, for) were implemented and tested successfully.  
The outputs matched the expected results, verifying correct program execution.  





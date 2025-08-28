

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

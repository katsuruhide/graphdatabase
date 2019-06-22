
"""logical operation    論理演算"""

def negation_operation(x):
    return (~x)

def conjunction_operation(x, y):
    return (x & y)

def disjunction_operation(x, y):
    return (x | y)

def implication_operation(x, y):
    return (~x | y)
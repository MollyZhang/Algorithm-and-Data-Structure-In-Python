"""
http://interactivepython.org/courselib/static/pythonds/Recursion/pythondsProgrammingExercises.html
Question 14
"""
import random
import pprint
import itertools



W = None
# each item in example is a tuple
# first item in the tuple is weight
# second item in the tuple is value
BOOK_EXAMPLE = [(2,3),(3,4), (4,8),(5,8),(9,10)]
SELECTION1 = None
SELECTION2 = []

def art_thief():
    example = generate_example_without_repeat(10, 30)
    print "example: ", example
    print "v1=========================================="
    print "max value of example: ", no_memoization_recursive_v1(example, W)
    print "selected items: ", find_selection_v1(SELECTION1, example)
    print "v2=========================================="
    print "max value of example: ", no_memoization_recursive_v2(example, W)
    print "selected items: ", SELECTION2






def generate_example_without_repeat(n, w):
    """based on given W and number of items, generate an appropriate example"""
    example = []
    global W
    W = w
    for i in range(n):
        weight = random.randint(1, w/2)
        value = random.randint(weight, weight*2)
        while (weight, value) in example:
            weight = random.randint(1, w/2)
            value = random.randint(weight, weight*2)
        example.append((weight, value))

    return example

def no_memoization_recursive_v1(example, W):
    """
    implementing this:
    M(E(n), W) = max(1<=i<=n) { V(n) + M(E(n) - E(i), W - w(n))}
    """

    if len(example) == 0 or W <= 0:
        return 0
    else:
        values = []
        for i in range(len(example)):
            (weight, value) = example[i]
            if weight > W:
                pass
            else:
                # python list is always pass by reference
                # therefore one cannot use example.pop(i) or example.remove()
                new_example = example[0:i] + example[(i+1):]
                values.append(value + no_memoization_recursive_v1(new_example, W - weight))
        global SELECTION1
        SELECTION1 = values
        if len(values) == 0:
            return 0
        else:
            return max(values)


def no_memoization_recursive_v2(example, W):
    """
    implementing this:
    M(E(n), W) = max { v(n)+ M(E(n-1),W-w(n)), M(E(n-1),w) }
    """
    if len(example) == 0 or W <= 0:
        return 0
    else:
        new_example = example[:-1]
        (weight, value) = example[-1]
        if weight > W:
            return no_memoization_recursive_v2(new_example, W)
        else:
            choice1 = value + no_memoization_recursive_v2(new_example, W - weight)
            choice2 = no_memoization_recursive_v2(new_example, W)
            global SELECTION2
            if choice1 > choice2 and example[-1] not in SELECTION2:
                SELECTION2.append(example[-1])
            return max(choice1, choice2)



def find_selection_v1(values, example):
    """
    any tuple item in the example list that gives out max value is
    selected as final output
    """
    selected_example = []
    for i in range(len(values)):
        if values[i] == max(values):
            selected_example.append(example[i])
    return selected_example

def find_selection_v2(selection):
    return selection


def memoization_non_recursive(example, W):
    pass


def get_all_sublists(lst):
    """
    return all combination of items of given list as a dictionary
    keys are number of items
    values are a list of the items of length key
    """
    n = len(lst)
    combinations = {}
    for length in range(1, len(lst)+1):
        combination = list(itertools.combinations(lst, length))
        combination.sort()
        combinations[length] = list(set(combination))
    return combinations


if __name__ == "__main__":
    art_thief()
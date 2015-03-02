"""
http://interactivepython.org/courselib/static/pythonds/Recursion/pythondsProgrammingExercises.html
Question 14
"""

W = 20
# each item in example is a tuple
# first item in the tuple is weight
# second item in the tuple is value
BOOK_EXAMPLE = [(2,3),(3,4), (4,8),(5,8), (9,10)]
SELECTION = 1

def art_thief():
    print no_memoization_recursive(BOOK_EXAMPLE,W)
    print SELECTION

def generate_example(n):
    pass


def no_memoization_recursive(example, W):
    if len(example) == 0 or W <= 0:
        return 0
    else:
        values = []
        for i in range(len(example)):
            value = example[i][1]
            weight = example[i][0]
            if weight > W:
                pass
            else:
                # python list is always pass by reference
                # therefore one cannot use example.pop(i) or example.remove()
                new_example = example[0:i] + example[(i+1):]
                values.append(value + no_memoization_recursive(new_example, W - weight))
        if len(values) == 0:
            return 0
        else:
            return max(values)




def memoization_non_recursive():
    pass


if __name__ == "__main__":
    art_thief()
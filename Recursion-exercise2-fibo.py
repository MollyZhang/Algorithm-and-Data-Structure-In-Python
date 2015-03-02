"""
Write a recursive function to compute the Fibonacci sequence.
How does the performance of the recursive function compare to that of an iterative version?
"""
import timeit

def main():
    n = 100
    print fibo_recursive(n)
    print fibo_iterative(n)
    comparison(n)

def fibo_recursive(n):
    """create fibonacci sequence"""
    if n == 1 or n == 2:
        return [1]*n
    last_list = fibo_recursive(n-1)
    return last_list + [last_list[-1] + last_list[-2]]

def fibo_iterative(n):
    fibo = [1,1]
    for i in range(1, n-1):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo

def comparison(n):
    test_rec = timeit.Timer("fibo_recursive(%d)" %n, setup="from __main__ import fibo_recursive")
    time_rec = test_rec.timeit(number=10000)
    test_ite = timeit.Timer("fibo_iterative(%d)" %n, setup="from __main__ import fibo_iterative")
    time_ite = test_ite.timeit(number=10000)
    print "recursive time: ", time_rec
    print "iterative time: ", time_ite




if __name__ == "__main__":
    main()

from __future__ import print_function
import random
import time

def main():
    maxN = 5
    n = list()
    for i in range(maxN):
        n.append(10**i)
    print(n)

    for j in n:
        a_list = random_list(j)

        for k in range(5):
            start1 = time.time()
            O_nsquare_sort(a_list)
            end1 = time.time()
            time1 = (end1 - start1)

        for k in range(5):
            start2 = time.time()
            O_n_sort(a_list)
            end2 = time.time()
            time2 = (end2-start2)

        print("N = ", "%6d" %j, "\t", "selection sort time = ", "%1.6f" %time1, "\t", "radix sort time = ", "%1.6f" %time2)


def O_nsquare_sort(a_list):
    """ selection sort    """
    b_list = list()
    copy_a = a_list[:]

    while len(copy_a)!=0:
        min_position = 0
        lmin = copy_a[0]
        for i in range(len(copy_a)):
            if copy_a[i] < lmin:
                lmin = copy_a[i]
                min_position = i
        copy_a.pop(min_position)
        b_list.append(lmin)
    return b_list

def O_n_sort(a_list, base=10):
    """ a simple immplementation of radix sort
    source: http://en.wikipedia.org/wiki/Radix_sort#Example_in_Python
    """
    def list_to_buckets(a_list, base, iteration):
        buckets = [[] for _ in range(base)]
        for number in a_list:
            # Isolate the base-digit from the number
            digit = ( number // (base ** iteration) ) % base
            # Drop the number into the correct bucket
            buckets[digit].append(number)
        return buckets

    def buckets_to_list(buckets):
        array = []
        # Collapse buckets back into a list
        for bucket in buckets:
            array.extend(bucket)
        return array

    # Find the largest value in the a_list to
    maxval = 0
    for i in a_list:
        if i > maxval:
            maxval = i

    it = 0
    # Iterate, sorting the a_list by each base-digit
    while ( (base ** it) <= maxval):
        a_list = buckets_to_list(list_to_buckets(a_list, base, it))
        it += 1

    return a_list


def random_list(n):
    """randomly generate a list of n numbers """
    a_list = list()
    for i in range(n):
        a_list.append(random.randint(0, 100000))
    return a_list

if __name__=="__main__":
    main()

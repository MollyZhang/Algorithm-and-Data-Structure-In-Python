import time
from matplotlib import pyplot as plt
import random

def empty(*args):
    pass

def list_index_operation(alist,index):
    alist[index]


def dictionary_get_operation(adict, index):
    adict.get(index)

def del_in_list(alist, index):
    del alist[index]

def del_in_dict(adict, key):
    del adict[key]


if __name__ == "__main__":

    maxN = []
    y1 = []
    y2 = []
    for i in range(1, 100000, 100):
        maxN.append(i)

###### Devise an experiment to verify that the list index operator is O(1) #######
    # for n in maxN:
    #     alist = range(n)
    #     random_index = random.randint(0, n-1)
    #     start1 = time.time()
    #     for repeat in range(100):
    #         list_index_operation(alist, random_index)
    #     end1 = time.time()
    #
    #     start2 = time.time()
    #     for repeat in range(100):
    #         empty(alist, random_index)
    #     end2 = time.time()
    #
    #     y1.append(end1-start1-(end2-start2))
    #
    # plt.plot(maxN,y1)
    # plt.show()

######## Devise an experiment to verify that get item and set item are O(1) for dictionaries.
    # for n in maxN:
    #     adict = {}
    #     for j in xrange(n):
    #         adict[j] = None
    #
    #     random_index = random.randint(0, n-1)
    #     start1 = time.time()
    #     for repeat in range(100):
    #         dictionary_get_operation(adict, random_index)
    #     end1 = time.time()
    #
    #     start2 = time.time()
    #     for repeat in range(100):
    #         empty(adict, random_index)
    #     end2 = time.time()
    #
    #     y1.append(end1-start1-(end2-start2))
    #
    # plt.plot(maxN,y1)
    # plt.show()

######### Devise an experiment that compares the performance of the del operator on lists and dictionaries.
    # for n in maxN:
    #     alist = range(n)
    #     adict = {}
    #     for j in xrange(n):
    #         adict[j] = None
    #     random_index = random.randint(0, n-1)
    #
    #     start1 = time.time()
    #     del_in_list(alist, random_index)
    #     end1 = time.time()
    #
    #     start2 = time.time()
    #     del_in_dict(adict, random_index)
    #     end2 = time.time()
    #
    #     start3 = time.time()
    #     empty(adict, random_index)
    #     end3 = time.time()
    #
    #     y1.append(end1-start1-(end3-start3))
    #     y2.append(end2-start2-(end3-start3))
    #
    # plt.plot(maxN,y1, "r--", maxN, y2)
    # plt.show()

#### Given a list of numbers in random order, write an algorithm that works in O(nlog(n))
#### to find the kth smallest number in the list.


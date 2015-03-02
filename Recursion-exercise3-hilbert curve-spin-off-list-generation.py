#############################################################################################
# experiments with concepts: generate a list of 4*n items using recursion and non-rescursion

def recursive_list_generation(n):
    if n == 1:
        return [1,2,3,4]
    else:
        new_list = []
        for sub_list in chop_up_to_4s(recursive_list_generation(n-1), n-1):
            new_list = new_list + generate_16_from_4(sub_list)
        return new_list

def non_recursive_list_generation(n):
    start_list = [1,2,3,4]
    last_level = []
    this_level = []
    if n == 1:
        return start_list
    else:
        for i in range(1,n+1):
            # a list at level n can be divided into 4^(n-1) sublists
            # each sublist containing four numbers
            if i == 1:
                this_level = start_list
            else:
                this_level = []
                sublists = chop_up_to_4s(last_level, i)
                for each_list in sublists:
                    this_level = this_level + generate_16_from_4(each_list)
            last_level = this_level
    return this_level


def generate_16_from_4(list4):
    list16 = []
    list_sum = sum(list4)
    for item in list4:
        for i in range(4):
            list16.append(list_sum * item + i)
    return list16

def chop_up_to_4s(list, n):
    """
    Chop up a list of level n (length 4^n) to 4^(n-1) sublists with 4 items
    """
    sublists = []
    num_sublists = 4**(n-1)
    for i in range(num_sublists):
        sublists.append(list[4*i: 4*i + 4])
    return sublists

def main1():
    print non_recursive_list_generation(2)
    print non_recursive_list_generation(3)
    print recursive_list_generation(2)
    print recursive_list_generation(3)

if __name__ == "__main__":
    main1()
    
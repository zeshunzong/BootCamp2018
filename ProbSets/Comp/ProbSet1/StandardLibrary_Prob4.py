import itertools
#given A is set
def get_power_set(A):
    num_of_element = len(A)
    power_set = [{}]
    #\emptyset is always in the power set
    #find the full combinations consisting of elements from 1 to all elements
    for i in range(1,num_of_element+1):
        temp = list(itertools.combinations(A, i))
        #temp is a list of tuples, where each tuple has i elements
        for t in temp:
            power_set.append(set(t))
        #convert each tuple to a set
    return power_set

print(get_power_set({1,2,3}))
print("We cannot have a set of set, because mutable objects cannot be put into a set, as they are not hashable.")

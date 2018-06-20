integer = 3
integer_prime = integer
integer_prime +=1
print(integer, integer_prime)
#int is immutable

string = "abc"
string_prime = string
string_prime += "d"
print(string, string_prime)
#str is immutable

list1 = [1,2,3]
list2 = list1
list2.append(4)
print(list1, list2)
#list is mutable

tuple1 = (1,2,3)
tuple2 =  tuple1
tuple2 += (1,)
print(tuple1, tuple2)
#tuple is immutable

set1 = {1,2,3}
set2 = set1
set2.add(4)
print(set1, set2)
#set is mutable

print("int is immutable \nstr is immutable \nlist is mutable")
print("tuple is immutable \nset is mutable")

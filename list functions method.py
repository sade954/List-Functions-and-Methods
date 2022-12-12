#Adding items to a list
my_list = [1, 2, 3]
my_list.append(4)
my_list
[1, 2, 3, 4]

#Inserting an item to a list
my_list.insert(0, 'a')
my_list
['a', 1, 2, 3, 4]

#Showing an idex of an item in a list
my_list = [1, 2, 3]
my_list.index(2)
1

#The "in" operation
my_list = [1, 2, 3]
4 in my_list
False
4 not in my_list
True

#Sorting List
my_list = [1, 3, 4, 8, 2]
sorted(my_list)
[1, 2, 3, 4, 8]

#Reversing a List
my_list = [1, 3, 4, 8, 2]
list(reversed(my_list)
[2, 8, 4, 3, 1]

#Revert list from high to low numbers in a list
my_list = [1, 3, 4, 8, 2]
list(reversed(sorted(my_list)))
[8, 4, 3, 2, 1]



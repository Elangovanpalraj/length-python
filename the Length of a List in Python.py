# the Length of a List in Python
# Using len() function
# Using Naive Method
# Using length_hint()
# Using sum() method
# Using a list comprehension
# Using recursion
# Using enumerate function
# Using Collections Module
# ----------------------------------------\n
# Using len() function
# ---------------------\n
li = [20,30.10,68]
n = len(li)
print("The length of list is:",n)
print('  ')
# Using Naive Method
# -------------------\n

test1 = [2,3,56,7,8,34,56]
print("The list is :" + str(test1))
counter = 0
for i in test1:
    counter = counter + 1

print("length using naive methods nis :" + str(counter))
print(" ")
# Using length_hint()
# ------------------\n

from operator import length_hint
test_list = [9,3,5,6,7,8,3,1]
print("the list is :" + str(test_list))
print(' ')
list_len = len(test_list)
list_len_hint = length_hint(test_list)
print("using len() is:" + str(list_len))
print("using length_hint() is :" + str(list_len_hint))

print(" ")
# Using sum() method
# ------------------\n
test_list = [1,2,4,5,6,8]
print('The list is:' + str(test_list))
list_len = sum(1 for i in test_list)
print('using len()is:'+str(list_len))
print('using length_hint()is:'+ str (list_len))
print(' ')
# Using a list comprehension
# --------------------------\n
test1 = [23,56,78,98,54,43,23]
length = sum(1 for _ in  test1)
print("using list comprehension is:",length)
print(' ')
#  List Using Recursion
# ---------------------\n
def count_elements_recursion(lst):
    if not lst:
        return 0
    return 1 + count_elements_recursion(lst[1:])
lst = [23,43,56,76,89,21,34,98]
print('list is length : ',count_elements_recursion(lst))
print(' ')
# List Using enumerate()
# --------------------\n
list1 = [45,6,78,9,3,4,23,45,34]
s = 0
for i ,a in enumerate(list1):
    s += 1
print('len is :',s)
print(' ')
#  List Using Collections
# -----------------------\n
from collections import Counter
test = [1,23,4,56,8,9]
list_len = sum(Counter(test).values())
print('using Counter()is:',list_len)
print(' ')
# Naive vs Python len() vs Python length_hint()
# ---------------------------------------------\n
from operator import length_hint
import time
 
# Initializing list
test_list = [1, 4, 5, 7, 8]
 
# Printing test_list
print("The list is : " + str(test_list))
 
# Finding length of list
# using loop
# Initializing counter
start_time_naive = time.time()
counter = 0
for i in test_list:
 
    # incrementing counter
    counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)
 
# Finding length of list
# using len()
start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)
 
# Finding length of list
# using length_hint()
start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)
 
# Printing Times of each
print("Time taken using naive method is : " + end_time_naive)
print("Time taken using len() is : " + end_time_len)
print("Time taken using length_hint() is : " + end_time_hint)
print('#-----------------------------------------------\n')
































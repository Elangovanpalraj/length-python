# Check if element exists in list in Python
# -----------------------------------------\n
# Input: test_list = [1, 6, 3, 5, 3, 4]
# 3  # Check if 3 exist or not.
# Output: True
# Explanation: The output is True because the element we are looking is exist in the list.
# --------------------------------------------------------------------------------------\n
# type
# -----\n
# Using “in” Statement 
# Using a loop 
# Using any() function
# Using count() function
# Using sort with bisect_left and set()
# Using find() method
# Using Counter() function
# Using try-except block
# --------------------------\n
# Using “in” Statement
# --------------------\n
lst = [21,4,8,6,5,56,89]
i = 4
if i in lst:
    print('exist')
else:
    print('not exist')

print(' ')
test = [1,3,6,7,9,4]
result = any(item in test for item in test)
print('Does string contain any list element:' + str (bool(result)))
print(' ')
# Using count() function
# ---------------------\n

test1 = [10, 15, 20, 7, 46, 2808]
print("checking if 20 exists in list")
exist_count = test1.count(20)
if exist_count > 0:
    print("yes, 20 exists in list")

else:
    print("No,20 does not exists in list")

print(' ')
# the list using a loop
# --------------------\n
# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

# Checking if 4 exists in list
for i in test_list:
    if(i == 4):
        print("Element Exists")
print(' ')
# the list using any()
# -------------------\n
# Initializing list
test_list = [1, 6, 3, 5, 3, 4]

result = any(item in test_list for item in test_list)
print("Does string contain any list element : " +str(bool(result)))
print(' ')
# the list using sort with bisect_left and set
# --------------------------------------------\n
from bisect import bisect_left , bisect
test_list_set = [ 1, 6, 3, 5, 3, 4 ]
test_list_bisect = [ 1, 6, 3, 5, 3, 4 ]
print("Checking if 4 exists in list ( using set() + in) : ")
test_list_set =set(test_list_set)
if 4 in test_list_set :
    print ("Element Exists")

print("Checking if 4 exists in list ( using sort() + bisect_left() ) : ")
# Checking if 4 exists in list 
# using sort() + bisect_left()
test_list_bisect.sort()
if bisect_left(test_list_bisect, 4)!=bisect(test_list_bisect, 4):
    print ("Element Exists")
else:
    print("Element doesnt exist")




















        

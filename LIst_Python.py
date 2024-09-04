#creating a list
numbers = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]
#iterate using a for loop
for num in numbers:
    print(num)
#iterate using a for loop and range
for i in range(len(numbers)):
    print(numbers[i])
    # List comprehension
squared_numbers = [num**2 for num in numbers]
print(squared_numbers)
for index, num in enumerate(numbers):
    print(f"Index: {index}, value: {num}")
    #iter function and next function
iterator = iter(numbers)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    #Map function
def square(num):
    return num**2
squared_numbers = list(map(square,numbers))
print(squared_numbers)
#Using zip
list1 = [1,2,3]
list2 = ['a','b','c',]
zipped= zip(list1, list2)
for item in zipped:
    print(item)
#using numpy module
import numpy as np
np_numbers=np.array(numbers)
print(np_numbers)
#example operation
squared_np_numbers = np_numbers ** 2
print(squared_np_numbers)
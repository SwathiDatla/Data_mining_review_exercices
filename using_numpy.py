import numpy as np

# Defining the list and convert in to a NumPy array list
numbers = [1225, 4986, 6789, 7890, 2345, 6783, 987, 1234, 8765, 3456]
np_numbers = np.array(numbers)

# Square of each element in the NumPy array list
squared_np_numbers = np_numbers ** 2

# Print the squared numbers
print(squared_np_numbers)

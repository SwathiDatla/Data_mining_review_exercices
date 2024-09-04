# Defining matrices
A = [[3.7827, 3.3454, 3.2341], [2.2122, 3.5678, 3.9087], [1.1234, 2.8934, 5.9087]]
B = [[3.1234, 3.0987, 3.1234], [2.1111, 3.2222, 3.3333], [1.0987, 1.3456, 5.1234]]
C = [[3.1243, 3.0989, 3.1256], [2.6721, 3.6785, 3.9017], [1.1254, 2.8956, 5.9187]]

# Functions to adding two matrices
def add_matrices(X, Y):
    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result

# Functions to subtracting two matrices
def subtract_matrices(X, Y):
    result = [[X[i][j] - Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result

# Functions to multiplying two matrices
def multiply_matrices(X, Y):
    result = [[sum(X[i][k] * Y[k][j] for k in range(len(Y))) for j in range(len(Y[0]))] for i in range(len(X))]
    return result

# Perform operations
sum_AB = add_matrices(A, B)
diff_AB = subtract_matrices(A, B)
prod_AB = multiply_matrices(A, B)

print("Sum of A and B:", sum_AB)
print("Difference of A and B:", diff_AB)
print("Product of A and B:", prod_AB)

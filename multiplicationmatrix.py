A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [7, 8],
    [9, 10],
    [11, 12]
]
rows_A = len(A)
cols_A = len(A[0])
rows_B = len(B)
cols_B = len(B[0])
if cols_A != rows_B:
    raise ValueError("Number of columns in A must be equal to number of rows in B")
result = []
for i in range(rows_A):
    result.append([])
    for j in range(cols_B):
        result[i].append(0)
for i in range(rows_A):
    for j in range(cols_B):
        for k in range(cols_A):
            result[i][j] += A[i][k] * B[k][j]
print("Product of matrices A and B:")
for i in range(len(result)):
    print(result[i])

n = int(input())
m = int(input())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        s = 0

        if i > 0:
            s += A[i-1][j]
        if i < n-1:
            s += A[i+1][j]
        if j > 0:
            s += A[i][j-1]
        if j < m-1:
            s += A[i][j+1]

        if A[i][j] > s:
            print(i, j, A[i][j])


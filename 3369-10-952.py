matrix = []
while True:
    n = str(input())
    if n == 'end':
        break
    matrix.append([int(s) for s in n.split()])
out_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):

        st = len(matrix)
        stlb = len(matrix[0])
        out_matrix[i][j]=int(matrix[i-1][j]) + int(matrix[(i+1)%st][j]) + int(matrix[i][j-1]) + int(matrix[i][(j+1)%stlb])

#вывод результата
for i in range(len(out_matrix)):
    for j in range(len(out_matrix[i])):
        print(out_matrix[i][j],end = ' ')
    print()

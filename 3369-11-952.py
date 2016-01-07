side = int(input())

'''заполняем квадратную матрицу нулями'''
matrix = [[0 for j in range(0, side)] for i in range(0, side)]

def go(chetnost):
    number = 1
    stroka = 0
    stolbec = side-1
    n=1

    while number < side**2-chetnost:
        for k in range(0, 2):
            for j in range(stroka, stolbec, n):
                matrix[stroka][j] = number
                number +=1

            for i in range(stroka, stolbec, n):
                matrix[i][stolbec] = number
                number +=1

            stroka,stolbec = stolbec,stroka
            n = n*(-1)
            k+=1

        stroka +=1
        stolbec -=1
if side%2 == 0:
    go(1)

else:
    go(0)
    matrix[int(side/2)][(int(side/2))] = side**2

'''выводим матрицу на экран'''
for i in range(0, side):
    for j in range(0, side):
        print(matrix[i][j], end=" ")
    print()
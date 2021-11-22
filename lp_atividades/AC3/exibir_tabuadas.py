A = int(input())
B = int(input())

if A <= B:
    for i in range(A, B + 1):
        for j in range(1, 11):
            print(i, 'x', j, '=', i * j)
        print('----------')
else:
    print('Nenhuma tabuada no intervalo!')
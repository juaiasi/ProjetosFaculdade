inicio = int(input())
fim = int(input())
primos = 0
for i in range(inicio, fim + 1):
    div = 0
    for j in range(1, i + 1):
        if i % j == 0:
            div += 1
    if div == 2:
        primos += 1
        print(i)

print(f'primos: {primos}')

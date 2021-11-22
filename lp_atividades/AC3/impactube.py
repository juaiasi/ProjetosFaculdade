n = int(input())
canais = [[]]*n
for i in range(n):
    canais[i] = input().split(';')
    canais[i][1] = int(canais[i][1])
    canais[i][2] = float(canais[i][2])
x = float(input())
y = float(input())

print('-----\nBÔNUS\n-----')
for canal in canais:
    bonus = canal[1]//1000
    if canal[3] == 'sim':
        bonus *= x
    else:
        bonus *= y
    print(f'{canal[0]}: R$ {canal[2]+bonus:.2f}')

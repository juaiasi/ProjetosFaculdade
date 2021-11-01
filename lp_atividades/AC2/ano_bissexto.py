inicio = int(input())
fim = int(input())

bissextos = 0
for i in range(inicio, fim + 1):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        print(i)
        bissextos += 1
    
print(f'bissextos: {bissextos}')
    
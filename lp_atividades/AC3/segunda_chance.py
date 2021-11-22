n = int(input())
notas = []
for i in range(n*2):
    notas.append(float(input()))

alteradas=0
for i in range(n):
    if notas[i+n] == 10 and notas[i] < 10:
        alteradas += 1
        
print('NOTAS ALTERADAS:',alteradas)

for i in range(n):
    if notas[i+n] == 10 and notas[i] < 10:
        nota_final = notas[i] + 2
        if nota_final > 10:
            nota_final = 10
        print(f'*({(i+1):03.0f}) original: {notas[i]:05.2f} | final: {nota_final:05.2f}')
    else:
        print(f'-({(i+1):03.0f}) original: {notas[i]:05.2f} | final: {notas[i]:05.2f}')

corridas = []
while True:
    corrida = int(input())
    if corrida >= 0:
        corridas.append(corrida)
    else:
        break
media = sum(corridas) / len(corridas)
print(f'MEDIA: {media:.2f}')
for corrida in corridas:
    if corrida < media:
        print(corrida)

doacao = float(input())
doacoes = []
while doacao != -1.0:
    doacoes.append(doacao)
    doacao = float(input())
total = 0
for doacao in doacoes:
  total = total + doacao
print(f'VC$ {total:.2f}')
print(f'R$ {(total*2.5):.2f}')
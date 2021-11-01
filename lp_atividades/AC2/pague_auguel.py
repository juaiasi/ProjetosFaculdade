divida = int(input())
mensalidade = int(input())
parcelas = divida//mensalidade
counter = 1
while divida != 0:
    print(f'pagamento: {counter}')
    print(f'antes = {divida}')
    if divida < mensalidade:
        divida = 0
    else:
        divida -= mensalidade
    print(f'depois = {divida}')
    print('-----')
    counter += 1

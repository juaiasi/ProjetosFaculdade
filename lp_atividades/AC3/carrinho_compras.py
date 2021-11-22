carrinho = list(map(int, input().split()))

while True:
    carrinho.sort()
    comando = input()
    if 'adicionar' in comando:
        l = comando.split()
        l[1] = int(l[1])
        carrinho.append(l[1])
    elif 'remover' in comando:
        l = comando.split()
        l[1] = int(l[1])
        if l[1] in carrinho:
            carrinho.remove(l[1])
        else:
            print(f'código {l[1]} não encontrado')
    elif comando == 'exibir':
        print(*carrinho, sep = " ")
    elif comando == 'encerrar':
        print(*carrinho, sep = " ")
        break

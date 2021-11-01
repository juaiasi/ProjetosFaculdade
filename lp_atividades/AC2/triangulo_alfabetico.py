linhas = int(input())
letra = 65 # esse número é a letra A
for n in range(1,linhas+1,1):
    print(chr(letra)*n)
    letra += 1

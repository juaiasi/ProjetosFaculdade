nota_trab = float(input())
nota_prova = float(input())
media = (nota_trab+nota_prova)/2
if media >= 6:
  print(f'aprovado')
elif (nota_trab+10)/2 >= 6:
  print(f'talvez com a sub')
else:
  print(f'reprovado')
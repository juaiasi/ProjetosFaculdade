dia_semana = input()
entrega = int(input())
semana = ['domingo','segunda','terca','quarta','quinta','sexta','sabado']
dia_entrega = semana.index(dia_semana)+entrega
if entrega == 0:
    print(f'chega hoje!')
else:
    if dia_entrega >= len(semana):
      dia_entrega -= len(semana)
    print(f'sera entregue {semana[dia_entrega]}')
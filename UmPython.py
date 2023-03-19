#declaração de duas listas dentro de uma:
#uma lista conterá números pares e outra números impares 
num = [[], []] 
valor = 0
quantidade = 0
soma = 0
for i in range(1, 6):
    valor = int(input(f'Digite o {i}º valor: '))
    soma += valor
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
media = soma / 5
print('-=' * 30)
print(f'valores pares digitados foram: {num[0]}')
print(f'valores pares digitados foram: {num[1]}')
print(f'Média geral dos valores digitados: {media}')

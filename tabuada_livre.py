num = int(input('Digite um número para verificar sua tabuada: '))
cont = 0

for i in range(0, 11):
    print(f'{num} x {cont} = {num * cont}')
    cont += 1

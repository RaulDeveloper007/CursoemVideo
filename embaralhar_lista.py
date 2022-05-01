import random
nome1 = input('Digite o nome do aluno: ')
nome2 = input('Digite o nome do aluno: ')
nome3 = input('Digite o nome do aluno: ')
nome4 = input('Digite o nome do aluno: ')
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)
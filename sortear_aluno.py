import sorteio
nome1 = input('Digite o nome do aluno: ')
nome2 = input('Digite o nome do aluno: ')
nome3 = input('Digite o nome do aluno: ')
nome4 = input('Digite o nome do aluno: ')
sorteio = [nome1, nome2, nome3, nome4]
escolhido  = random.choice(sorteio)
print(f'O escolhido para apagar o quadro foi: {escolhido}.')
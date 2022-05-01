km = float(input('Quantos km o carro percorreu? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
aluguel = (dias * 60) + (km * 0.15)
print(f'O preço a pagar pelo aluguel do carro é: R${aluguel:.2f}')

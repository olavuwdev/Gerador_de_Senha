import random
import csv

upper_case = 'ABCDEFGHIJKLMOPQRSTUXYWZ'
low_case = upper_case.lower()
number = '1234567890'
caracters = '*&$#@!*()+{^`'
size = 8

key = low_case + upper_case + number + caracters

password = "".join(random.sample(key, size))
print(f'Sua senha segura é {password}')

arquivo = open('password.txt', 'a', newline='')
dados = []
dados.append(password)
gravador = csv.writer(arquivo)
gravador.writerow(dados)

arquivo.close()

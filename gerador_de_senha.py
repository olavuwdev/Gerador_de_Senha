import random

low_case = 'ABCDEFGHIJKLMOPQRSTUXYWZ'
upper_case = low_case.upper()
number = '1234567890'
caracters = '*&$#@!*()+{^`'
size = 8

key = low_case + upper_case + number + caracters

password = "".join(random.sample(key, size))

import random

def sorteio(pessoas):
    sortudo = random.choice(pessoas)
    print(f'A pessoa sortuda é : {sortudo}')

pessoas = []

for x in range(5):
    nome = input(f'digite o {x + 1 }º nome ')
    pessoas.insert(0,nome)
    
sorteio(pessoas)
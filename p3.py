numero_1 = int(input('digite o numero 1 : '))

numero_2 = int(input('digite o numero 2 : '))

numero_3 = int(input('digite o numero 3 : '))

if numero_1>numero_2 and numero_1>numero_3:
    print(f' O numero 1 é maior {numero_1}:' )
    
elif numero_2>numero_1 and numero_2>numero_3:
    print(f'O numero 2 é maior {numero_2}: ')
    
else:
    print(f'O numero 3 é maior {numero_3}: ')
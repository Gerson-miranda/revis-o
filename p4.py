numero = int(input('digite o numero : '))

operador = input('digite o operador + - * / : ')

for x in range(1,11):
    
    if(operador == '+'):
    
     calculo = numero + x
    
     print(f'{numero} + {x} = {calculo} : ')
     
    elif(operador == '-'):
    
     calculo = numero - x
    
     print(f'{numero} - {x} = {calculo} : ')
     
    elif(operador == '*'):
    
     calculo = numero * x
    
     print(f'{numero} * {x} = {calculo} : ')
     
    elif(operador == '/'):
    
     calculo = numero / x
    
     print(f'{numero} / {x} = {calculo} : ')
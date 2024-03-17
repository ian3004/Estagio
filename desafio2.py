def is_fibonacci(num):
   
    if num == 0:
        return True
    elif num == 1:
        return True
    
   
    a, b = 0, 1
    
  
    while b < num:
        a, b = b, a + b
        

    if b == num:
        return True
    else:
        return False


numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))


if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

def proximo_elemento(sequencia):
   
    if len(sequencia) == 1:
        return sequencia[0]
 
    elif len(sequencia) == 2:
        return sequencia[0] + sequencia[1]
   
    else:
     
        return sequencia[-1] + (sequencia[-1] - sequencia[-2])


sequencias = [
    [1, 3, 5, 7],
    [2, 4, 8, 16, 32, 64],
    [0, 1, 4, 9, 16, 25, 36],
    [4, 16, 36, 64],
    [1, 1, 2, 3, 5, 8],
    [2, 10, 12, 16, 17, 18, 19]
]

for sequencia in sequencias:
    print("Sequência:", sequencia)
    proximo = proximo_elemento(sequencia)
    print("Próximo elemento:", proximo)
    print()


import time

def descobrir_interruptores():
    # primeiro interruptor sendo ligado
    print("Ligando o primeiro interruptor...")
    time.sleep(2)  # Aguarda alguns segundos para simular o tempo passando
    
    #primeiro interruptor sendo desligado e o segundo interruptor sendo ligado
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")
    time.sleep(2)  # Aguarda alguns segundos para simular o tempo passando
    
    #  entrada na sala para verificar as lâmpadas
    print("Você entra na sala e observa as lâmpadas:")
    print("1ª lâmpada:", "Acesa")
    print("2ª lâmpada:", "Fria e Apagada")
    print("3ª lâmpada:", "Apagada e Quente")


descobrir_interruptores()
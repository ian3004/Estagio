def inverter_string(string):
  
    string_invertida = ""

   
    for i in range(len(string) - 1, -1, -1):
       
        string_invertida += string[i]

    return string_invertida


minha_string = "Hello, world!"
string_invertida = inverter_string(minha_string)
print("String original:", minha_string)
print("String invertida:", string_invertida)

entrada = input("Digite um palavra: ")
vogais = ["a", "e", "i", "o", "u"]
contador = 0
consoantes = []
for i in entrada:
  if i in vogais:
    pass
  else:
    contador += 1
    consoantes.append(i)  
print("Foram lidas ", contador, " consoantes")
print(consoantes)

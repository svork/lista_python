entrada = input("Digite 20 números: ")
vetor = entrada.split()
par = []
impar = []
for i in vetor:
  if int(i) % 2 == 0:
    par.append(i)  
  else:
    impar.append(i)  
print(vetor)
print(par)
print(impar)

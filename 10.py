vetor1 = input("Digite alguns numeros: ")
v1 = set()
for i in vetor1:
  v1.add(i)
vetor2 = input("Digite alguns numeros: ")
v2 = set()
for i in vetor2:
  v2.add(i)
vetor3 = v1.intersection(v2)
print(vetor3)

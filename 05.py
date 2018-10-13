total_eleitores = int(input("Digite o total de eleitores: "))
candidato_0 = 0
candidato_1 = 0
candidato_2 = 0
def votar():
  global candidato_0
  global candidato_1
  global candidato_2
  print("Digite o número do candidato escolhido")
  print("Candidato 0 = 0")
  print("Candidato 1 = 1")
  print("Candidato 2 = 2")
  voto = int(input("Número do candidato: "))
  if voto == 0:
    candidato_0 += 1
  elif voto == 1:
    candidato_1 += 1
  elif voto == 2:
    candidato_2 += 1
  else:
    print("Voto inválido")
while total_eleitores > 0:
  votar()
  total_eleitores -= 1
print("O candidato 0 teve ", candidato_0, " votos")
print("O candidato 1 teve ", candidato_1, " votos")
print("O candidato 2 teve ", candidato_2, " votos")

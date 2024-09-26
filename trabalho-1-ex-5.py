# informe o nome do aluno
nome = input("Nome do aluno: ")

# disciplinas: História, Geografia, Português, Matemática, Ciências, Literatura
maria = [5.6, 6.7, 7.0, 10.0, 4.0, 8.0]
tania = [2.3, 6.6, 8.0, 5.5, 10.0, 5.0]
jose = [7.7, 4.0, 7.0, 7.9, 2.2, 6.5]
daniel = [9.0, 10.0, 3.3, 8.0, 6.0, 4.6]

if nome == "Maria":
  notas = maria
elif nome == "Tânia":
  notas = tania
elif nome == "José":
  notas = jose
elif nome == "Daniel":
  notas = daniel
else:
  notas = []

if notas == []:
  print("Aluno inexistente")

else:
  media = (notas[0] + notas[1] +notas[2] +notas[3] +notas[4] +notas[5]) / 6

  print(f"Notas do aluno(a) {nome}:\n")
  print("História: ", notas[0])
  print("Geografia: ",notas[1])
  print("Português: ",notas[2])
  print("Matemática: ",notas[3])
  print("Ciências: ",notas[4])
  print("Literatura: ",notas[5])
  print(f"\nMédia: {media:.1f}")

  if media >= 5.0:
    print("Aluno aprovado")
  else:
    print("Aluno reprovado")

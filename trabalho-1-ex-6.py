quantidade_funcionarios = int(input("Quantidade de funcionários: "))
funcionarios = []
soma_salarios = 0
soma_idades = 0
contador = 1

while contador <= quantidade_funcionarios:
  print(f"\nFuncionário {contador}:")
  nome = input("Nome: ")
  salario = float(input("Salário: "))
  ano_nascimento = int(input("Ano de nascimento: "))
  idade = 2024 - ano_nascimento

  soma_salarios = soma_salarios + salario
  soma_idades = soma_idades + idade
  funcionarios.append([nome, salario, ano_nascimento, idade])

  contador = contador + 1

media_salarios = soma_salarios / quantidade_funcionarios
media_idades = soma_idades / quantidade_funcionarios

print("\nFuncionários:")

contador = 0
while contador < quantidade_funcionarios:
  print(contador + 1, funcionarios[contador])
  contador = contador + 1

print(f"Média dos salários: {media_salarios:.2f}")
print(f"Média das idades: {media_idades:.2f}")

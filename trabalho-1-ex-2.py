funcionário = input("Nome: ")
idade = input("Idade: ")
endereço = input("Endereço: ")
função = input("Cargo: ")
salário = float(input("Salário: "))

print("Nome do funcionário: ", funcionário)
print("Idade do funcionário: ", idade)
print("Endereço completo: ", endereço)
print("Cargo do funcionário: ", função)
print("Salário anterior: ", salário)

salário = salário + (salário * 0.25)

print("Salário reajustado em 25%: ", salário)

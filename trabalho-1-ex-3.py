# quantidade dos itens
quantidade_arroz = 5
quantidade_feijão = 3
quantidade_açúcar = 2
quantidade_batata = 3
quantidade_óleo = 5
quantidade_bolacha_de_água_e_sal = 1
quantidade_bolacha_de_maizena = 1
quantidade_banana = 1.5
quantidade_couve_flor = 2
quantidade_leite_em_pó = 2

# preço unitário dos itens
preço_unitário_arroz = float(input("Preço unitário do arroz: "))
preço_unitário_feijão = float(input("Preço unitário do feijão: "))
preço_unitário_açúcar = float(input("Preço unitário do acúcar: "))
preço_unitário_batata = float(input("Preço unitário da batata: "))
preço_unitário_óleo = float(input("Preço unitário do oleo: "))
preço_unitário_bolacha_de_água_e_sal = float(input("Preço unitário da bolacha de água e sal: "))
preço_unitário_bolacha_de_maizena = float(input("Preço unitário da bolacha de maizena: "))
preço_unitário_banana = float(input("Preço unitário da banana: "))
preço_unitário_couve_flor = float(input("Preço unitário da couve-flor: "))
preço_unitário_leite_em_pó = float(input("Preço unitário do leite em pó: "))

# mostrar os valores no console
print(f"Preço unitário do arroz: {preço_unitário_arroz:.2f}")
print(f"Preço unitário do feijão: {preço_unitário_feijão:.2f}")
print(f"Preço unitário do acúcar: {preço_unitário_açúcar:.2f}")
print(f"Preço unitário da batata: {preço_unitário_batata:.2f}")
print(f"Preço unitário do oleo: {preço_unitário_óleo:.2f}")
print(f"Preço unitário da bolacha de água e sal: {preço_unitário_bolacha_de_água_e_sal:.2f}")
print(f"Preço unitário da bolacha de maizena: {preço_unitário_bolacha_de_maizena:.2f}")
print(f"Preço unitário da banana: {preço_unitário_banana:.2f}")
print(f"Preço unitário da couve-flor: {preço_unitário_couve_flor:.2f}")
print(f"Preço unitário do leite em pó: {preço_unitário_leite_em_pó:.2f}")

# total de cada item
preço_arroz = quantidade_arroz * preço_unitário_arroz
preço_feijão = quantidade_feijão * preço_unitário_feijão
preço_açúcar = quantidade_açúcar * preço_unitário_açúcar
preço_batata = quantidade_batata * preço_unitário_batata
preço_óleo = quantidade_óleo * preço_unitário_óleo
preço_bolacha_de_agua_e_sal = quantidade_bolacha_de_água_e_sal * preço_unitário_bolacha_de_água_e_sal
preço_bolacha_de_maizena = quantidade_bolacha_de_maizena * preço_unitário_bolacha_de_maizena
preço_banana = quantidade_banana * preço_unitário_banana
preço_couve_flor = quantidade_couve_flor * preço_unitário_couve_flor
preço_leite_em_pó = quantidade_leite_em_pó * preço_unitário_leite_em_pó

# mostrar os valores no console
print(f"Preço do arroz: {preço_arroz:.2f}")
print(f"Preço do feijão: {preço_feijão:.2f}")
print(f"Preço do acúcar: {preço_açúcar:.2f}")
print(f"Preço da batata: {preço_batata:.2f}")
print(f"Preço do oleo: {preço_óleo:.2f}")
print(f"Preço da bolacha de água e sal: {preço_bolacha_de_agua_e_sal:.2f}")
print(f"Preço da bolacha de maizena: {preço_bolacha_de_maizena:.2f}")
print(f"Preço da banana: {preço_banana:.2f}")
print(f"Preço da couve-flor: {preço_couve_flor:.2f}")
print(f"Preço do leite em pó: {preço_leite_em_pó:.2f}")

# total da compra
total = preço_arroz + preço_feijão + preço_açúcar + preço_batata + preço_óleo + preço_bolacha_de_agua_e_sal + preço_bolacha_de_maizena + preço_banana + preço_couve_flor + preço_leite_em_pó

# mostrar o total no console
print("Total da compra: ", total)

# limite em dinheiro
limite = float(input("Limite em dinheiro: "))

# se o total é menor que o limite: pagamento em dinheiro
if total <= limite:
  print("pagamento em dinheiro")

# se o total é maior que o limite: pagamento em parcelas com uso de cartão
if total > limite:
  print("pagamento em parcelas com uso de cartão")

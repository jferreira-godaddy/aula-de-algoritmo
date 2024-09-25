# ler as variáveis
temperatura = float(input("Temperatura: "))
umidade_relativa_do_ar = float(input("Umidade Relativa do Ar: "))
estação_do_ano = input("Estação do Ano (primavera/verão/outono/inverno): ")
previsão = "dados insuficientes para a previsão do tempo"

# mostrar os valores no console
print(f"Temperatura: {temperatura:.2f}")
print(f"Umidade Relativa do Ar: {umidade_relativa_do_ar:.2f}")
print(f"Estação do Ano: {estação_do_ano}")

# Se (Temperatura ≥ 28ºC e Umidade Relativa do Ar ≥ 50% e Estação do Ano = verão OU primavera)
if temperatura >= 28 and umidade_relativa_do_ar >= 50 and (estação_do_ano == "verão" or estação_do_ano == "primavera"):
  previsão = "irá chover amanhã"
# Se (Temperatura ≤ 16ºC e Umidade Relativa do Ar ≥ 80% e Estação do Ano = outono OU inverno)
if temperatura <= 16 and umidade_relativa_do_ar >= 80 and (estação_do_ano == "outono" or estação_do_ano == "inverno"):
  previsão = "irá chover amanhã"
# Se (Temperatura < 9ºC e Umidade Relativa do Ar < 50% e Estação do Ano = outono OU inverno)
if temperatura < 9 and umidade_relativa_do_ar < 50 and (estação_do_ano == "outono" or estação_do_ano == "inverno"):
  previsão = "amanhã o dia será sem chuvas"
# Se (Temperatura > 26ºC e Umidade Relativa do Ar ≤ 40% e Estação do Ano = verão OU primavera)
if temperatura > 26 and umidade_relativa_do_ar <= 40 and (estação_do_ano == "verão" or estação_do_ano == "primavera"):
  previsão = "amanhã o dia será sem chuvas"

# mostrar a previsão do tempo para o dia seguinte
print("Previsão do tempo para o dia seguinte: ", previsão)

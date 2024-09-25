condição = True # False
temperatura_manhã = 17 # 13
temperatura_noite = 10
temperatura_tarde = 19

while condição:
  if temperatura_manhã > temperatura_noite: # 17 > 10
    temperatura_manhã = 13
    print("temperatura_manhã = ", temperatura_manhã)
    print("temperatura_tarde = ", temperatura_tarde)
    print("temperatura_noite = ", temperatura_noite)
    condição = not True
  else:
    temperatura_tarde >= 0 and temperatura_noite <= 11
    if temperatura_noite < 10:
      temperatura_noite = 11
      print("temperatura_manhã = ", temperatura_manhã)
      print("temperatura_tarde = ", temperatura_tarde)
      print("temperatura_noite = ", temperatura_noite)
      condição = False
    else:
      if temperatura_manhã == 17 or temperatura_noite > 20:
        temperatura_tarde = 21
        print("temperatura_manhã = ", temperatura_manhã)
        print("temperatura_tarde = ", temperatura_tarde)
        print("temperatura_noite = ", temperatura_noite)
        condição = not False

print("condição = ", condição)


def classificar_preco(preco):
    if preco >= 100:
        return "preco caro"

    elif preco >= 50:
        return "preco normal"

    else:
        return "barato"


precos = [30, 80, 120, 45, 200]

for preco in precos:
    resulto = classificar_preco(preco)
    print(resulto)
     

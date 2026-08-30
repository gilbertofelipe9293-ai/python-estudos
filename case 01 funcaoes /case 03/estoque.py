estoque = {
    "Arroz": {
        "quantidade": 10,
        "preco": 20
    },
    "Feijao": {
        "quantidade": 5,
        "preco": 8
    },
    "Milho": {
        "quantidade": 0,
        "preco": 6
    }
}


def verificar(produto):

    if produto in estoque:

        quantidade = estoque[produto]["quantidade"]
        preco = estoque[produto]["preco"]

        return produto, quantidade, preco

    else:
        return "Produto não localizado"


produto = input("Busque um produto: ")

resultado = verificar(produto)

print(resultado)

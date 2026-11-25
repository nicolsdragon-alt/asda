nome_cliente = input("Digite seu nome: ").strip()

print("\n--- CARDÁPIO DE COMBOS ---")
print("1 - Clássico da Casa (R$ 24,99)")
print("2 - Crocante do Dia  (R$ 29,99)")
print("3 - Duplo Sabor      (R$ 34,99)")
print("4 - Fit & Fresh      (R$ 39,99)")
print("5 - Kids Divertido   (R$ 19,99)")

combo = input("\nDigite o número do combo desejado (1 a 5): ").strip()

match combo:
    case "1":
        nome_combo = "Combo 1 – Clássico da Casa"
        descricao = (
            "- X-Burguer (pão, hambúrguer bovino, queijo, alface, tomate e maionese)\n"
            "- Batata frita pequena\n"
            "- Refrigerante lata (350 ml)"
        )
        preco = 24.99
    case "2":
        nome_combo = "Combo 2 – Crocante do Dia"
        descricao = (
            "- 6 unidades de frango empanado (nuggets ou tiras crocantes)\n"
            "- Porção de batata smiles ou batata frita média\n"
            "- Suco natural de laranja (300 ml)"
        )
        preco = 29.99
    case "3":
        nome_combo = "Combo 3 – Duplo Sabor"
        descricao = (
            "- X-Bacon Duplo (pão, 2 hambúrgueres bovinos, queijo cheddar, bacon, alface, maionese especial)\n"
            "- Onion rings (6 unidades)\n"
            "- Refrigerante 500 ml"
        )
        preco = 34.99
    case "4":
        nome_combo = "Combo 4 – Fit & Fresh"
        descricao = (
            "- Sanduíche natural (peito de frango desfiado, cenoura, alface, tomate e maionese light)\n"
            "- Salada de frutas\n"
            "- Água mineral ou suco detox"
        )
        preco = 39.99
    case "5":
        nome_combo = "Combo 5 – Kids Divertido"
        descricao = (
            "- Mini hot dog (salsicha, molho, queijo ralado e batata palha)\n"
            "- Mini batata frita\n"
            "- Suco de uva\n"
            "- Brinde surpresa"
        )
        preco = 19.99
    case _:
        preco = None

if preco is None:
    print("\nOpção de combo inválida! Escolha um número de 1 a 5.")
else:
    print(f"\n{nome_combo} — R$ {preco:.2f}")
    print(descricao)

    quantidade = int(input("\nDigite a quantidade desejada: "))

    if quantidade <= 0:
        print("\nQuantidade inválida! Digite pelo menos 1 unidade.")
    else:
        total = preco * quantidade
        print("\n--- RESUMO DO PEDIDO ---")
        print(f"Cliente: {nome_cliente}")
        print(f"Item: {nome_combo}")
        print(f"Quantidade: {quantidade}")
        print(f"Valor total a pagar: R$ {total:.2f}")
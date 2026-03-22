print("-----------------Cardápio--------------------")
print("---------------------------------------------")
print("---| Tamanho | Cupuaçu (C)  |  Açaí (A) |----")
print("---|    P    |   R$ 9,00    | R$ 11,00  |----")
print("---|    M    |   R$ 14,00   | R$ 16,00  |----")
print("---|    G    |   R$ 18,00   | R$ 20,00  |----")
print("---------------------------------------------")

acp = 7.00
acm = 9.00
acg = 11.00
cpp = 5.00
cpm = 7.00
cpg = 9.00
valor_total= 0
name = input("Bem vindo(a) ao Açaí Zuri, qual é o seu nome? ")
print(f"Olá {name}, seja bem vindo(a), o que deseja pedir?")

# TAMANHO
while True:
    while True:
        tamanho = input("Escolha o tamanho do seu pedido: [P/M/G]: ").upper().strip()
        if tamanho == "P":
            print("Você escolheu o tamanho Pequeno")
            break
        elif tamanho == "M":
            print("Você escolheu o tamanho Médio")
            break
        elif tamanho == "G":
            print("Você escolheu o tamanho Grande")
            break
        else:
            print("Insira um valor válido")

# SABOR
    while True:
        sabor = input("Escolha o sabor do seu pedido: [C/A]: ").upper().strip()
        if sabor == "C":
            print("Você escolheu o sabor Cupuaçu")
            break
        elif sabor == "A":
            print("Você escolheu o sabor Açaí")
            break
        else:
            print("Insira um valor válido")
# VALOR INICIAL
    if sabor == "C":
        if tamanho == "P":
            valor = cpp
        elif tamanho == "M":
            valor = cpm
        elif tamanho == "G":
                valor = cpg
    
    elif sabor == "A":
        if tamanho == "P":
            valor = acp
        elif tamanho == "M":
            valor = acm
        elif tamanho == "G":
            valor = acg
    valor_total += valor
    while True:
        escolha = input("Deseja adicionar mais algum item ao pedido? [S/N]").upper()
        if escolha == "S":
            break
        elif escolha == "N":
            break
        else:
            print("Insira um valor valido")
    if escolha == "N":
        break

print(f"Valor total do pedido: R$ {valor_total:.2f}")

# ENTREGA
entrega = input("Insira seu endereço para entrega: ")
print(f"Obrigado por pedir conosco, {name}! A Zuri agradece! Seu pedido será entregue em {entrega} em breve.")

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

name = input("Bem vindo(a) ao Açaí Zuri, qual é o seu nome? ")
print(f"Olá {name}, seja bem vindo(a), o que deseja pedir?")

# TAMANHO
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
    else:
        valor = cpg
elif sabor == "A":
    if tamanho == "P":
        valor = acp
    elif tamanho == "M":
        valor = acm
    else:
        valor = acg

print(f"O valor do seu pedido é R$ {valor:.2f}")

# COMPLEMENTOS
acrescentar = input("Deseja acrescentar algo mais? [S/N]: ").upper().strip()

if acrescentar == "S":

    # SABOR 2
    while True:
        sabor2 = input("Sabor do complemento [C/A]: ").upper().strip()
        if sabor2 == "C":
            print("Você escolheu Cupuaçu")
            break
        elif sabor2 == "A":
            print("Você escolheu Açaí")
            break
        else:
            print("Valor inválido")

    # TAMANHO 2
    while True:
        tamanho2 = input("Tamanho do complemento [P/M/G]: ").upper().strip()
        if tamanho2 == "P":
            break
        elif tamanho2 == "M":
            break
        elif tamanho2 == "G":
            break
        else:
            print("Valor inválido")

    # VALOR DO COMPLEMENTO
    if sabor2 == "C":
        if tamanho2 == "P":
            valor2 = cpp
        elif tamanho2 == "M":
            valor2 = cpm
        else:
            valor2 = cpg

    elif sabor2 == "A":
        if tamanho2 == "P":
            valor2 = acp
        elif tamanho2 == "M":
            valor2 = acm
        else:
            valor2 = acg

    # SOMA
    valor += valor2

elif acrescentar == "N":
    print("Pedido sem complemento")

else:
    print("Valor inválido")

print(f"Valor total do pedido: R$ {valor:.2f}")

# ENTREGA
entrega = input("Insira seu endereço para entrega: ")
print(f"Obrigado por pedir conosco, {name}! A Zuri agradece! Seu pedido será entregue em {entrega} em breve.")

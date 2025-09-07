#Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#Combustível	Quantidade Vendida	Desconto por Litro
#Álcool	Até 25 litros	10%
#Álcool	Acima de 25 litros	20%
#Gasolina	Até 25 litros	15%
#Gasolina	Acima de 25 litros	30%
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

import os
os.system("cls")


print("""
    COMBUSTÍVEL: \t|  QUANTIDADE VENDIDA: \t| DESCONTO POR LITRO:
    Álcool\t\t| Áte 25 litros\t\t| 10%
    Álcool\t\t| Acima de 25 litros \t| 20%
    Gasolina\t\t| Áte 25 litros\t\t| 15%
    Gasolina\t\t| Acima de 25 litros\t| 30%

      """)

preco_alcool = 3.79
preco_gasolina = 6.59

litros = float(input("Digite a quantidade de litros: "))
tipo_combustivel = input("Digite o tipo de combustível (a para álcool, g para gasolina): ")

valor = 0
valor_total = 0
desconto = 0

if tipo_combustivel == 'a':
    valor = litros * preco_alcool
    if litros <= 25:
        desconto = valor * 0.10
    else:
        desconto = valor * 0.20
elif tipo_combustivel == 'g':
    valor = litros * preco_gasolina
    if litros <= 25:
        desconto = valor * 0.15
    else:
        desconto = valor * 0.30
else:
    print("Tipo de combustível inválido.")
    exit()


valor_total = valor - desconto


print(f"O valor a ser pago é: R$ {valor_total:.2f}")

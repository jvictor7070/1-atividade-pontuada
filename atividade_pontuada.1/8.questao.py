#Em uma loja de CD's existem apenas quatro tipos de preços que estão associados a cores. 
# Assim, os CD's que ficam na loja não são marcados por preços e sim por cores. 
# Desenvolva um algoritmo que, a partir da entrada da cor, o software mostre o preço. 
# A loja está atualmente com a seguinte tabela de preços:

#Cor    	Preço
#Verde	    R$ 10,00
#Azul	    R$ 20,00
#Amarelo	R$ 30,00
#Vermelho	R$ 40,00


import os
os.system("cls")

print("""
    COR: \t|  PREÇO:
    verde\t| R$10,00
    azul\t| R$20,00
    amarelo\t| R$30,00
    vermelho\t| R$40,00

      """)

cor = input("digite a cor do disco: ")
valor = float
quantia = int(input("quantidade desejada de disco:"))

match cor:
    case "verde":
        valor = 10.00
    case "azul":
        valor = 20.00
    case "amarelo":
        valor = 30.00
    case "vermelho":
        valor = 40.00
    case _:
        print("Cor inválida. Por favor, digite uma das cores da lista.")

valor_total = quantia * valor        


print(f"""
cor do disco: {cor}""")
print(f"valor do disco: {valor}")
print(f"valor total: {valor_total}")





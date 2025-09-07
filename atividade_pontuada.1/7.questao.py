#Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida e o preço unitário. 
# Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto e o total a pagar (total a pagar = total - desconto), sabendo-se que:
#Se quantidade <= 5, o desconto será de 2%.
#Se quantidade > 5 e quantidade <= 10, o desconto será de 3%.
#Se quantidade > 10, o desconto será de 5%.



import os
os.system("cls")

nome = input("descrição do produto: ")
quantidade_adquirida = int(input("quantidade desejada: "))
preco_unitario  = float(input("valor do produto:R$ "))
desconto = float

total = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
   desconto = total * 0.02
elif quantidade_adquirida > 5 and quantidade_adquirida <= 10:
  desconto = total * 0.03
elif quantidade_adquirida > 10: 
  desconto = total * 0.05
else:
  print("desconto não aplicado")

total_a_pagar = total - desconto

print(f"""
descrição do produto: {nome}""")      
print(f"quantidade adquirida: {quantidade_adquirida}")      
print(f"valor do produto: {preco_unitario:.2f}")      
print(f"desconto aplicado: R${desconto:.2f}")      
print(f"total a pagar: {total_a_pagar:.2f}")      
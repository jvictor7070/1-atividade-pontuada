#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#Fruta	Até 5 Kg	Acima de 5 Kg
#Morango	R$ 2,50 por Kg	R$ 2,20 por Kg
#Maçã	R$ 1,80 por Kg	R$ 1,50 por Kg
#Se o cliente comprar a partir de 10 Kg em frutas ou o valor total da compra ultrapassar R$ 15,00, receberá ainda um desconto de 10% sobre este total. 
# screva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.

import os
os.system("cls")

print("""
      Fruta  \t|  até 5 kg  \t| acima de 5 kg
      morango\t|  R$2,50 por kg\t| R$2,20 por kg
      Maçãs\t|  R$1,80 por kg\t| R$1,50 por kg
      """)

fruta = input("qual fruta gostaria de comprar: ")
quantia = int(input("qual a quantidade(kg): "))
preco = float

match fruta:
    case "maçãs":
        if quantia >=6:
            preco  = quantia * 1.80 
        else:
            preco = quantia * 1.50  

        if quantia >= 10:
         desconto = preco * 0.10
         valortotal = preco - desconto
        elif preco >= 15:
            desconto = preco * 0.10
            valortotal = preco - desconto
        else:
            print("fim") 

            desconto = preco * 0.10
            valortotal = preco - desconto 
               
            print(f"""
fruta escolhida: {fruta}""")
            print(f"quantidade: {quantia}kg")
            print(f"fruta escolhida: {fruta}")
            print(f"valor original: {preco:.2f}")        
            print(f"desconto aplicado: R${desconto:.2f}(10%)")        
            print(f"valor total: {valortotal:.2f}")   
        
    case "morangos":
        if quantia >=6:
            preco  = quantia * 2.20 
        else:
            preco = quantia * 2.50 

        if quantia >= 10:
         desconto = preco * 0.10
         valortotal = preco - desconto
        elif preco >= 15:
            desconto = preco * 0.10
            valortotal = preco - desconto     
        else:
            print("fim")    

            desconto = preco * 0.10
            valortotal = preco - desconto 
            
            print(f"""
fruta escolhida: {fruta}""")
            print(f"quantidade: {quantia}kg")
            print(f"fruta escolhida: {fruta}")
            print(f"valor original: {preco:.2f}")        
            print(f"desconto aplicado: R${desconto:.2f}(10%)")        
            print(f"valor total: {valortotal:.2f}")   
    case _:
        print("""
fruta não se encontra no catálogo.""")  

#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C, caso contrário, imprima que A + B é maior que C.

import os
os.system("cls")

a = float(input("digite o valor de a: "))
b = float(input("digite o valor de b: "))
c = float(input("digite o valor de c: "))
soma = a + b
print(f"valor da soma:{soma}")

if soma < c:
    print("""
a soma de A + B é menor que C.""")
elif soma > c:
    print("""
a soma de A + B é maior que C.""")
else:
    print("""
a soma de A + B é igual a C.""")    


print("fim!")
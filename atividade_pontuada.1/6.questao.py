#Escreva um programa que leia do teclado as duas notas de um aluno, calcule e exiba a média aritmética das notas.
#O programa deve, adicionalmente, exibir uma mensagem de parabéns caso o aluno esteja aprovado (média superior ou igual a 6,0); 
# caso a média esteja entre 4,1 e 5,9, o aluno está em recuperação; caso a média seja inferior a 4,0, o aluno será reprovado.


import os
os.system("cls")


nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("digite a segunda nota: "))

soma = nota_1 + nota_2
media = soma / 2



print(f"média: {media}")

if media >= 6:
    print("Parabéns, você foi aprovado.")
elif media >=4.1 <=5.9:
    print("você está de recuperação.") 
else:
    print("você foi reprovado. ")


#Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso o sexo seja “F” e o estado civil seja “CASADA”, solicitar o tempo de casada (em anos). Por fim, mostre os dados do usuário.

import os
os.system("cls")


nome = input("digite seu nome: ")
print("digite F para feminino ou M para masculino.")
sexo = input("digite seu gênero:")
estado_civil = input("digite seu estado civil: ")

match sexo:
    case "f":
        if estado_civil == "casada":
            casamento = input("duração do casamento:")

            print(f"nome: {nome}")
            print(f"gênero: feminino ({sexo})")
            print(f"estado civil: {estado_civil}")
            print(f"duração do casamento: {casamento}")
        
        else:
            print(f"nome: {nome}")
            print(f"gênero: feminino ({sexo})")
            print(f"estado civil: {estado_civil}")

    case "m":
        print(f"nome: {nome}")
        print(f"gênero: masculino ({sexo})")
        print(f"estado civil: {estado_civil}")

    case _:
        print("algo deu errado, por favor!! reinicie o processo.")    
        
        
    
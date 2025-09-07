#Uma financeira usa o seguinte critério para conceder empréstimos: 
# o valor total do empréstimo deve ser até dez vezes o valor da renda mensal do solicitante, e o valor da prestação deve ser no máximo 30% da renda mensal do solicitante. Escreva um programa que leia a renda mensal de um solicitante, o valor total do empréstimo solicitado e o número de prestações que o solicitante deseja pagar e informe se o empréstimo pode ou não ser concedido.

import os
os.system("cls")


# Entrada de dados
renda = float(input("Digite sua renda mensal: R$ "))
emprestimo = float(input("Digite o valor total do empréstimo : R$ "))
prestacoes = int(input("Digite o número de prestações: "))

# Critérios para concessão do empréstimo
limite_emprestimo = renda * 10
valor_prestacao = emprestimo / prestacoes
limite_prestacao = renda * 0.30

# Verificação das condições
if emprestimo <= limite_emprestimo and valor_prestacao <= limite_prestacao:
    print("O empréstimo pode ser concedido.")
    print(f"O valor de cada prestação será de R$ {valor_prestacao:.2f}.")
else:
    print("O empréstimo não pode ser concedido.")
    print(f"O valor máximo do empréstimo é de R$ {limite_emprestimo:.2f}.")
    print(f"O valor máximo da prestação é de R$ {limite_prestacao:.2f}.")

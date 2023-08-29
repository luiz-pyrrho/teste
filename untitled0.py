# -*- coding: utf-8 -*-
"""
Created on Thu May  4 21:00:39 2023

@author: luiz
"""

# RA: 159619  Aluno: Luiz Henrique Pyrrho Soares

# solicita ao usuário que informe a quantidade de notas a serem lidas
quantidade_notas = int(input("Digite a quantidade de notas a serem informadas: "))

# inicializa as variáveis de maior nota, menor nota e soma das notas
maior_nota = float('-inf')  # valor inicial é o menor valor possível
menor_nota = float('inf')  # valor inicial é o maior valor possível
soma_notas = 0

# lê cada nota individualmente e atualiza as variáveis de maior nota, menor nota e soma das notas
for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota
    soma_notas += nota

# calcula a média aritmética das notas
media = soma_notas / quantidade_notas

# exibe os resultados na tela
print(f"A maior nota informada foi {maior_nota}")
print(f"A menor nota informada foi {menor_nota}")
print(f"A média das notas informadas foi {media:.2f}")


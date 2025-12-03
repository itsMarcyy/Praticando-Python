'''
Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.'''

dia_a = int(input("Informe os dias para a atividade A: "))
dia_b = int(input("Informe os dias para a atividade B: "))
dia_c = int(input("Informe os dias para a atividade C: "))

if (dia_a >= 0 and dia_b >= 0 and dia_c >= 0):
    tempo_total = dia_a + dia_b + dia_c
    print(f"O tempo total do projeto é de {tempo_total} dias")
else:
    print("Erro: Número de dias negativos")
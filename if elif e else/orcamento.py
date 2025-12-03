'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
'''

limite = 3000.0
despesa_total = float(input("Informe qual foi a sua despesa mensal em R$: "))

if despesa_total <= limite:
    print("Você está dentro do orçamento!")
else:
    print("Atenção! Limite mensal ultrapassado.")
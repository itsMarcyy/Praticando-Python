'''
Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.
'''

temperatura = float(input("Digite a temperatura atual do servidor: "))

if (temperatura <=25):
    print("Tudo certo com a temperatura do servidor!")
else:
    print("Alerta! Temperatura acima do recomendado.")
# Calculadora de IMC
print("Bem-vindo à Calculadora de IMC!")

nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)
print(f"{nome}, seu IMC é: {imc:.2f}")
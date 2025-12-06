numeroDigitado = int(input("Digite um número (0 para parar): "))

numero = 0

while numeroDigitado != 0:
    numero += numeroDigitado
    numeroDigitado = int(input("Digite um número (0 para parar): "))

print(f"A soma dos números é: {numero}")
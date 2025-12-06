print("Bem-vindo(a) tabuada automática e personalizada")
numero = int(input("Digite um número: "))

seTemIntervalo = input("Tem intervalo? sim ou não ").lower
if seTemIntervalo == "sim":
    intervalo = int(input("Intervalo de: (num inteiro) "))

i = 1

while i <= 10:
    resultado *= i
    print(f"{numero} x {i} = numero")
    i += 1
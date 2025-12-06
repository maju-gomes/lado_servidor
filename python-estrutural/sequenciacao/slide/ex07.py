nome = input()

quantidade = len(nome)
linhaCimaBaixo = "+" + "-" * (quantidade + 2) + "+"

nome = f"| {nome} |"

print(linhaCimaBaixo)
print(nome)
print(linhaCimaBaixo)
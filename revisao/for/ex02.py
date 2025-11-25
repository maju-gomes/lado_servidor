frase = input("Digite uma frase: ").lower()

listaVogal= ["a", "e", "i", "o", "u"]
vogais = 0

for letra in frase:
    if letra in listaVogal:
        vogais += 1
    
if vogais > 1:
    print(f"Sua frase tem {vogais} vogais.")
else:
    print(f"Sua frase tem {vogais} vogal.")
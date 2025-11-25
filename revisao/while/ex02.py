senha = input("Senha: ")
confirmarSenha = input("Confirmar senha: ")

tentativas = 1 #porque o user já tentou uma vez

while confirmarSenha != senha and tentativas < 3:
    print("Sua senha está errada!")
    confirmarSenha = input("Confirmar senha: ")
    tentativas += 1

if senha == confirmarSenha:
    print("Senha confirmada")
else:
    print("Você chegou no limite de tentativas")
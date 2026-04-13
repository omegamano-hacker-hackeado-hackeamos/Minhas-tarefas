import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
senha = input("coloque sua senha:")
senha_armazenada = senha
random.choice(caracteres)
tamanho = int(input("tamanho da senha"))
for i in range(tamanho):
    senha + random.choice(caracteres)

print(senha)
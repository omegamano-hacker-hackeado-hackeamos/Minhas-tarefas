meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "bot":"pessoa ruim ou literalmente um robo"
            "AURA": "garbo"
            }
word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")
if word in meme_dict.keys():
    print(meme_dict.keys(word))
else:
    print("Palavra não encontrada")

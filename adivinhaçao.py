import random

# Gera um número aleatório entre 1 e 20
numero_secreto = random.randint(1, 20)

# Loop de 5 tentativas
for tentativa in range(1, 6):
    print("Tentativa {tentativa}: Adivinhe o número de 1 a 20:")
    
    chute = int(input())

    # Comparações
    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif chute < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
else:
  
    print(f"Não há mais tentativas. O número secreto era {numero_secreto}.")
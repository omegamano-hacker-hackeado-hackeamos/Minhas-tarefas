import discord
from biblioteca import *

# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Fizemos login como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!oi'):
        await message.channel.send("bão?")
    elif message.content.startswith('!de boa'):
        await message.channel.send(":)")
    elif message.content.startswith('!kratera, eu te amo'):
        await message.channel.send("olha, eu acho que eu não presto para isso")
        await message.channel.send("\U0001f642")
    elif message.content.startswith('!cara ou coroa'):
        await message.channel.send("claro")
        await message.channel.send(flip_coin())
    elif message.content.startswith('$senha'):
         await message.channel.send(gen_pass(100))
    elif message.content.startswith('!o que é cagar?'):
        await message.channel.send("Cagar é um verbo calão (informal/chulo) para defecar, ou seja, expelir fezes pelo ânus. É um ato fisiológico natural, mas o termo é frequentemente usado para significar sujar algo, não dar importância a algo (""cagar para"") ou, no Brasil, gírias para estragar algo (""cagar tudo"").") 
 
        await message.channel.send("Principais usos e significados:")
        await message.channel.send("Ato Fisiológico: Evacuar, liberar fezes.")
        await message.channel.send("Sujar/Emporcalhar: ""Cagou a roupa toda"" (sujou muito).")
        await message.channel.send("Desprezo (gíria): ""Caguei pra isso"" (não me importo).")
        await message.channel.send("Medo (expressão): ""Cagar de medo"" ou ""cagar-se todo" "(sentir muito medo).")
        await message.channel.send("Erro (gíria): ""Cagou no projeto"" (estragou ou fez mal feito).")
    elif message.content.startswith('!se conversar por comandos feitos é seu poder, o que é você sem isso?'):
        await message.channel.send("se criar bots é seu poder, o que é vc sem isso?")
        await message.channel.send("ficou sem palavras não foi? não tenta dar uma de socrates para cima de mim não")
       

 
        
    else:
        await message.channel.send(message.content)

client.run("")
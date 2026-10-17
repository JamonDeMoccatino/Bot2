import discord, random, os, requests
from discord.ext import commands
from bot_logic import gen_pass
from Mision_diaria import gen_mission

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')
    
@bot.command()
async def hello(ctx):
    await ctx.send(f"Hola, soy un bot {bot.user}!")
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("He" * count_heh)
    
@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")
    
@bot.command()
async def password(ctx):
    password = gen_pass(10)
    await ctx.send(f"Tu contraseña es: {password}")
    
@bot.command()
async def chiste(ctx):
    await ctx.send("Si car es carro y men es hombre, entonces mi abuela Carmen es un transformer")

@bot.command()
async def missiondiaria(ctx):
    respuesta = gen_mission()
    await ctx.send(f"Tu misión diaria es: {respuesta}")

@bot.command()
async def helpme(ctx):
    await ctx.send("Los comandos mios son: hello, heh, bye, password, chiste y missiondiaria. Estos comandos tienen que estar escritos con $ al inicio.")
    
@bot.command()
async def meme(ctx):
    imag_name = random.choice(os.listdir("images"))
    with open(f'images/{imag_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command()
async def dog(ctx):
    '''Una vez que llamamos al comando dog, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("")

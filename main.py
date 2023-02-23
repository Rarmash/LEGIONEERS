import discord
from options import token
import os
import os.path

intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.messages = True

bot = discord.Bot(case_insensitive=True, intents=intents)

@bot.event
async def on_ready():
    print("------")
    print("Бот запущен!")
    print(f"Вошли как {bot.user.name}")
    print(f"ID бота: {str(bot.user.id)}")
    for guild in bot.guilds:
        print(f"Подключились к серверу: {guild}")
    print("------")
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="резню"))
    
for filename in os.listdir("./cogs"):
    if (
        filename.endswith(".py")
        and filename != "__init__.py"
        #and (filename != "events.py" or debugmode != "ON")
    ):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(token)
import json
import os
import disnake

from disnake.ext import commands
from createDB import create_db

with open('./master.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)

token = data["bot_info"]["token"]
cp = data["bot_info"]["cp"]

intents = disnake.Intents.all()

bot = commands.Bot(command_prefix=cp,intents=intents)

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.id == 779290532622893057:
            for channel in guild.text_channels:
                if channel.name == "bot_commands":
                    await channel.send('Gother Is Online!')

for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(filename, 'loaded')

@bot.command()
@commands.has_any_role('Team Owners', 'Owners', 'Head Dev', 'Head Developer','Head Admin','Head Administrator')
async def update(ctx):
    async def start():
        os.system("python ./bot.py")
        await confirm()
    await ctx.send("Gother will reset now")
    await start()

async def confirm(ctx):
    await ctx.send("Restart Complete")


if __name__ == '__main__':
    create_db()
    bot.run(token)
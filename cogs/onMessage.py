import disnake 
import sqlite3 as sql 
import asyncio 
import json

from disnake.ext import commands 

with open('./master.json','r',encoding='utf-8-sig') as f:
    data = json.load(f)
    
cp = data["bot_info"]["cp"]


class OnMessageEvents(commands.Cog):
    def __init__(self,bot):
        self.bot=bot 
        
        
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.content.startswith('prefix'):
            msg = await message.channel.send(f'Gothers\' Prefix Is `{cp}`')
            await asyncio.sleep(15)
            await msg.delete()
            
        elif message.content.startswith('data'):
            guild_icon = message.guild.icon
            
            if message.guild.icon is None:
                guild_icon = self.bot.user.avatar
                
            embed=disnake.Embed(
            color=disnake.Colour.random(),
            timestamp=message.created_at,
            title='Dont Ask To Ask',
            description='To Get Permission To Ask A Question, Please [Click Here :D](https://dontasktoask.com/)'
            ).set_thumbnail(
                url=guild_icon
            ).set_footer(
                text="Don't ask can you ask a question. Just ask it! :D"
            )
            
            msg = await message.channel.send(embed=embed)
            
            await asyncio.sleep(15)
            await msg.delete()


def setup(bot):
    bot.add_cog(OnMessageEvents(bot))
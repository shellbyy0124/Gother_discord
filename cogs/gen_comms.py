import asyncio as asyc
import sqlite3 as sql 
import disnake
import json

from disnake.ext import commands 
from disnake.ext.commands.errors import MissingRequiredArgument as MRA 
from disnake.ext.commands.errors import MissingPermissions as MP 
from disnake.ext.commands.errors import MemberNotFound as MNF
from disnake.ext.commands.slash_core import slash_command

class GeneralCommands(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
        
        
    @commands.slash_command(
        description="Returns Gothers' Latency"
    )
    async def ping(self,ctx,inter):
        with open('./master.json','r',encoding='utf-8-sig') as f:
            data = json.load(f)
            
        discInfo = data["bot_info"]["supp_disc"]
        
        embed=disnake.Embed(
            color=disnake.Colour.random(),
            timestamp=ctx.message.created_at,
            title="Gother's Latency Command",
            description=f'{round(self.bot.latency*1000)}ms\nIf you feel as though Gothers\' Latency is higher than normal, please [submit a ticket]({discInfo}) with a screenshot, and details of what was happening in the guild.'
        ).set_thumbnail(
            url=self.bot.user.avatar
        )
        
        await inter.reply(embed=embed)
        
        
    @commands.slash_command(
        description="Returns The FAQ Embed For Gother"
    )
    async def faq(self,ctx,inter):
        def check(i):
            return inter.author.id == i.author.id
        
        with open('./info.json','r',encoding='utf-8-sig') as f:
            data = json.load(f)
            
        vsPast = data['version']['past']
        vsCurrent = data['version']['current']
        vsFuture = data['version']['future']
        
        mek = [
            "Mekasu",
            data['devs']['mekasu']['discTag'],
            "Current Servers",
            [data['devs']['mekasu']['currentServers']['LearningTogether'],
                data['devs']['mekasu']['currentServers']['GotherSupport'],
                data['devs']['mekasu']['currentServers']['Shuffles']]]
        
        logPrevious = data['changeLog']['previous']
        logCurrent = data['changeLog']['current']
        logFuture = data['changeLog']['future']
        
        gotherHistory = data['history']['Gother']
        shufflesHistory = data['history']['Gother']
                
        embed1=disnake.Embed(
            color=disnake.Colour.random(),
            timestamp=ctx.message.created_at,
            title="Gothers' Frequently Asked Questions",
            description=f"""To come up with frequently asked questions with answers,
                            can sometimes become a very long and drawn out process
                            which is why instead of creating an FAQ site, search 
                            command, I decided to just build an embed that displayed 
                            various information that is written into a json file 
                            and is 100% editable by the dev staff of Gother only."""
        )
        
        embed2=disnake.Embed(
            color=disnake.Colour.random(),
            timestamp=ctx.message.created_at,
            title="Developers",
            description=f"""Name: {mek[0]}
                            Tag: {mek[1]}
                            Current Servers:
                            --[Learning Together]({mek[2][0]})
                            --[Gother Support]({mek[2][1]})
                            --[Shuffles]({mek[2][2]})
                        """
        )
        
        embed3=disnake.Embed(
            color=disnake.Colour.random(),
            timestamp=ctx.message.created_at,
            title="Change Logs",
            description=f"""Past: {logPrevious}
                            Current: {logCurrent}
                            Future: {logFuture}"""
        )
        
        embed4 = disnake.Embed(
            colour=disnake.Colour.random(),
            timestamp=ctx.message.created_at,
            title="Gothers History",
            description=f"{gotherHistory}"
        )
        
        embed5 = disnake.Embed(
            colour=disnake.Colour.random(),
            timestamp=ctx.message.created_at,
            title="Shuffles History",
            description=f"{shufflesHistory}"
        )
        
def setup(bot):
    bot.add_cog(GeneralCommands(bot))
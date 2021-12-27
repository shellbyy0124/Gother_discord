import disnake
import sqlite3 as sql
import asyncio
import json

from disnake.ext import commands


class OnMessageEvents(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message, inter):
        if message.author.id == self.bot.user.id:
            pass  # do not want bot responding to itself
        else:
            if message.content.startswith('prefix'):
                """
                fix this to check if 'prefix' is the only word in the message
                """
                cp = await self.getCp()  # call the module to get the command prefix

                msg = await (f'Gothers\' Prefix Is `{cp}`')
                await asyncio.sleep(15)  # give them time to read the message
                await msg.delete()  # clean up bot responses for nicer chat

            elif message.content.startswith('data'):
                guild_icon = message.guild.icon  # obtain guild id = easier to use

                if message.guild.icon is None:  # check if the guild has an icon
                    guild_icon = self.bot.user.avatar  # if not, use Gother's icon

                embed = disnake.Embed(
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

    async def getCp(self):
        """
        Instead of having functions above the class at the start of the script,
        I decided to start utilizing modules, or smaller functions that do 
        tiny jobs to make scripts run more efficiently (imo). 
        """
        with open('./master.json', 'r', encoding='utf-8-sig') as f:  # open a json file
            # load the json files' iformation into a variable for manipulation
            data = json.load(f)

        # obtain the specifically needed information
        cp = data["bot_info"]["cp"]

        return cp  # send the information back and stop the function


def setup(bot):
    """
    This function allows the commands above to be useable by the bot
    """

    bot.add_cog(OnMessageEvents(bot))

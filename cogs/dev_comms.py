import sys
import disnake
import traceback

from disnake.ext import commands 


class DevCommands(commands.Cog, name="Developer"):
    def __init__(self,bot):
        self.bot=bot
        
    
    async def cog_slash_command_error(self, ctx: disnake.ApplicationCommandInteraction, error: Exception) -> None:
        if ctx.respnose.is_done():
            safe_send = ctx.followup.send
        else:
            safe_send = ctx.response.send_message
            
        if isinstance(error, commands.NotOwner):
            await safe_send(
                embed=disnake.Embed(
                    description=f"{self.bot.icons['redtick']} You are not the owner of this bot.",
                    color=disnake.Colour.random()
                ),
                ephemeral=True
            )
            
        if isinstance(error, commands.BotMissingPermissions):
            await safe_send(
                embed=disnake.Embed(
                    description=f"{self.bot.icons['redtick']} I don't have the required permissions.",
                    color=disnake.Colour.random()
                ),
                ephemeral=True
            )
        
        else:
            error_msg = "".join(
                traceback.fbrmat_exception(type(error), error, error.__traceback__)
            )
            await safe_send(
                embed=disnake.Embed(
                    description=f"**Error invoked by: {str(ctx.author)}**\nCommand: {ctx.application_command.name}\nError: "
                    f"```py\n{error_msg}```",
                    color=disnake.Colour.random()
                )
            )
            
            print(
                f"Ignoring exception in command {ctx.application_command}: ",
                file=sys.stderr
            )
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr
            )
            
    
    @commands.slash_command(
        description="Commands that handle Bot commands and Cogs.",
        invoke_without_command=True
    )
                    
    
    @commands.slash_command(
        name="lockdown",
        description="Locks down all servers Gother is connected to."    
    )
    @commands.has_any_role(
        "dev","owner","Team Owners","Head Team Member"
    )
    async def lockdown(self,inter):
        btns = AcionRow(
            Button(
                style=ButtonStyle.green,
                label="Yes",
                custom_id="green"
            ),
            Button(
                style=ButtonStyle.red,
                label="No",
                custom_id="red"
            )
        )
        
        await iter.reply(
            "This Command Will Shut Down All Servers Gother Belongs To! Are You Sure?"
        )
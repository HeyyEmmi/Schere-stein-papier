import discord
from discord.ext import tasks, commands
import locale
import random


# TODO kms
class STP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() #Schere, stein, Papier
    async def stp(self, ctx, oshi):
        choices = ["schere", "stein", "papier"]
        choice = random.choice(choices)
        if(oshi.lower() in choices):
            embed = discord.Embed(title="Schere Stein Papier", colour=discord.Colour(0xa33b39))
            embed.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
            embed.add_field(name="Deine Wahl:", value=oshi.lower())
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="Bot Wahl:", value=choice)
            embed.add_field(name="\u200B", value="\u200B")
            embed.add_field(name="\u200B", value="\u200B")
            if(oshi.lower() == choice):
                embed.add_field(name="Unentschieden!", value="\u200B")
                embed.set_footer(text="Created by HeyyEmmi#0001 & Luby#0002")
            elif(oshi.lower() == "schere" and choice == "stein"):
                embed.add_field(name="Du hast verloren!", value="\u200B")
                embed.set_footer(text="Created by HeyyEmmi#0001 & Luby#0002")
            elif(oshi.lower() == "stein" and choice == "papier"):
                embed.add_field(name="Du hast verloren!", value="\u200B")
                embed.set_footer(text="Created by HeyyEmmi#0001 & Luby#0002")
            elif(oshi.lower() == "papier" and choice == "schere"):
                embed.add_field(name="Du hast verloren!", value="\u200B")
                embed.set_footer(text="Created by HeyyEmmi#0001 & Luby#0002")
            else:
                embed.add_field(name="Du hast gewonnen!", value="\u200B")
                embed.set_footer(text="Created by HeyyEmmi#0001 & Luby#0002")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Bitte nur mit \"schere\", \"stein\"oder \"papier\" antworten")
            


def setup(bot):
    bot.add_cog(STP(bot))

    

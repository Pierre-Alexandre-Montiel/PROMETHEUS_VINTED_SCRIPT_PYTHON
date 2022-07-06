import discord
from discord.ext import commands
import os, json


intents = discord.Intents().all()
bot = commands.Bot(command_prefix="$", intents=intents)
bot.remove_command("help")

try:
    os.system('cls')
except:
    os.system('clear')
with open("config.json", 'r') as config:
    configs = json.load(config)

@bot.event
async def on_ready():
    print('\n')
    print(f"Welcome to :")
    print("""
    
██████╗░██████╗░░█████╗░███╗░░░███╗███████╗████████╗██╗░░██╗███████╗██╗░░░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔════╝╚══██╔══╝██║░░██║██╔════╝██║░░░██║██╔════╝
██████╔╝██████╔╝██║░░██║██╔████╔██║█████╗░░░░░██║░░░███████║█████╗░░██║░░░██║╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██║╚██╔╝██║██╔══╝░░░░░██║░░░██╔══██║██╔══╝░░██║░░░██║░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝██║░╚═╝░██║███████╗░░░██║░░░██║░░██║███████╗╚██████╔╝██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝░╚═════╝░╚═════╝░
                          
        !$TheOneAndTheOnlyOne$!

    """)
   # print(f"Welcome to : {bot.user.name}")
    await bot.change_presence(activity=discord.Game(name="Script from : https://github.com/Prometheus"))


@bot.command()
async def find(ctx, vintedurl):
    x = await ctx.channel.create_webhook(name="Discord-test")
    with open("config.json", 'w+') as configedit:
        configs["suburl"][str(x.url)] = {}
        configs["suburl"][str(x.url)]["url"] = str(vintedurl)
        configs["suburl"][str(x.url)]["salon"] = str(ctx.channel.name)

        json.dump(configs,configedit,indent=4)
#    await ctx.send(f"{ctx.author.mention} - **✔️ Webhook ajouté avec le lien !**")
    await ctx.send(f"{ctx.author.mention} - **✔️ Research Completed !**")

@bot.command()
async def change_url(ctx, new_url):
    for weburl in configs["suburl"]:
        if configs["suburl"][weburl]["salon"] == ctx.channel.name:
            with open("config.json", 'w+') as configedit:
                configs["suburl"][str(weburl)]["url"] = str(new_url)
                json.dump(configs,configedit,indent=4)
            await ctx.send(f"{ctx.author.mention} - **✔️ Url well modified !**")
            return

@bot.command()
async def remove_url(ctx):
    webhook = None
    for weburl in configs["suburl"]:
        if configs["suburl"][weburl]["salon"] == ctx.channel.name:
            webhook = weburl
            with open("config.json", 'w+') as configedit:
                del configs["suburl"][webhook]
                json.dump(configs,configedit,indent=4)
            await ctx.send(f"{ctx.author.mention} - **✔️ Url well deteled !**")
            return

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Help Prometheus Bot",color=0xFFFFFF)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.add_field(name="**find**",value=f"**Usage :** ``{configs['prefix']}sub url_vinted``",inline=False)
    embed.add_field(name="**remove_sub**",value=f"**Usage :** ``{configs['prefix']}remove_sub``",inline=False)
    embed.add_field(name="**change_url**",value=f"**Usage :** ``{configs['prefix']}change_url nouvel_url_vinted``",inline=False)
    await ctx.send(embed=embed)

bot.run(configs["token"])

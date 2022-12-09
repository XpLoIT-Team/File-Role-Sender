import discord
from config import id_cargo, nome_do_pdf
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

global id_cargo
global nome_do_pdf

@bot.event
async def on_ready():
  print("AI PAPAI")
  await bot.change_presence(status=discord.Status.dnd)


@bot.command(pass_context=True)
async def env(ctx):
  role = get(ctx.guild.roles, id=id_cargo)    
  for user in ctx.guild.members:
    try:
      if role in user.roles:
        if user.dm_channel is None:
            await user.create_dm()
        # await user.dm_channel.send("hello")     Se quiser enviar uma mensagem a mais 
        await user.dm_channel.send(content="mamaquin",file=discord.File(rf'{nome_do_pdf}'))
    except:
      await ctx.send(f"```[DM]  {user.name}  🔐```")

bot.run("MTA1MDUxNTIyMjY1MTIxOTk4OA.GF0BMP.6Rn9PhaBoimgvZb4qYUFkl39LVyRcED02cgg-0")
token = "fart immediatedly"
import discord
from discord import app_commands
from discord.ext import commands #idk how important this one is

intents = discord.Intents.all()
client = commands.Bot(command_prefix="no", intents=intents)

@client.event
async def on_ready():
  print("bot is up and ready")
  try:
    synched = await client.tree.sync()
    print(f"Synched {len(synched)} commands")
  except:
    print("sucks")
@client.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
  await interaction.response.send_message(f"farded")
  
client.run(token)

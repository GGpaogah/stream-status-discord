import discord, os , alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='!',
  self_bot=True
)

@client.event
async def on_connect():
  await client.change_presence(activity = discord.Playing(name = 
  "With ur Mom"))
  
alive.alive()
client.run(os.getenv("TOKEN"), bot=False)

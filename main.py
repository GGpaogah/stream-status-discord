import discord, os , keep_alive , asyncio , datetime ,pytz


from discord.ext import tasks, commands

client = commands.Bot(
  command_prefix='zz!',
  self_bot=True
)




@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = 
  "abit sangat sadboy pemirsa", url = "https://twitch.tv/paogah"))



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)
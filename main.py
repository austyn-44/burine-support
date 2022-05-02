import discord
from discord.ext import commands

bot = commands.Bot(command_prefix= '=')

@bot.event 
async def on_ready():
   print("Im alive!")

@bot.listen('on_message')
async def stuff(message):
    if message.content.startswith("hi"):


      embed = discord.Embed(
        title = '',
        description = '''Hey, I'm Burnie Support

Please use the following command instead: .help

If you continue to have problems, consider asking for help [Click Here](https://discord.gg/aQ24CNtqrg)''',
        color = 0xFFFFFF
      )

      msg = await message.channel.send(embed=embed)
bot.run("OTcwMTkxNjQ3Mzg2MjQzMDcy.Gcsk5Z.JYt1NVa6R69c9_NBplJ8-3DXaunBCmFIcuept8")
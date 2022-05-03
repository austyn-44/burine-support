import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
intents = discord.Intents.default()
intents.members = True

PREFIX = ("-")
bot = commands.Bot(command_prefix=PREFIX, description='Hi')

@bot.event
async def on_ready():
    activity = discord.Game(name="Supporting Users!", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    username_1 = ctx.message.author.name
    avatar_1 = ctx.message.author.avatar_url
    await member.kick(reason=reason)
    embed=discord.Embed(description=f'👌 User {member} has been kicked',
    color = 0xffffff)
    embed.set_author(name=f"Requested by {username_1}", icon_url=avatar_1)
    await ctx.send(embed=embed)

@bot.listen('on_message')
async def stuff(message):
    if message.content.startswith("hi"):


      embed = discord.Embed(
        title = '',
        description = '''Hey, I'm Burnie Support

If you continue to have problems, consider asking for help [Click Here](https://discord.gg/XzjRHDt4VX)''',
        color = 0xFFFFFF
      )

      msg = await message.channel.send(embed=embed)

@bot.listen('on_message')
async def stuff(message):
    if message.content.startswith("invite"):


      embed = discord.Embed(
        title = '',
        description = '''Do you want To Invite **Burnie Bot** ? Click [here](https://discord.com/api/oauth2/authorize?client_id=970555340775112704&permissions=8&scope=bot%20applications.commands)''',
        color = 0xFFFFFF
      )

      msg = await message.channel.send(embed=embed)

@bot.listen('on_message')
async def stuff(message):
  if message.content.startswith("vote"):


    embed = discord.Embed(
      title = '',
      description = '''Do you want to vote **Burnie Bot** ? Click [here](https://discordbotlist.com/bots/burnie/upvote)''',
      color = 0xFFFFFF
    )

    msg = await message.channel.send(embed=embed)

@commands.command() # uses command decorators, in this case inside a cog
@commands.has_permissions(ban_members=True) # only people that have permissions to ban users can use this command
async def ban(self, ctx, user: discord.Member, *, reason): # The person banning someone has to ping the user to ban, and input a reason. Remove self if you are outside a cog.
    await ctx.guild.ban(user, reason=reason) # Bans the user.
    await user.send(f"🤦‍♂️ You have been banned in {ctx.guild} for {reason}") # Private messages user.
    await ctx.send(f"👌 {user} has been successfully banned.")

bot.run("OTcwMTkxNjQ3Mzg2MjQzMDcy.Gcsk5Z.JYt1NVa6R69c9_NBplJ8-3DXaunBCmFIcuept8")
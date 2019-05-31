import discord

from discord.ext import commands

class MyBot(commands.Bot):
    if __name__ == '__main__':
        bot = MyBot(command_prefix='/')
@bot.event
async def on_ready():
    print('ログインしました')
@bot.command(pass_context = True)
async def ban(member: discord.Member, days: int = 1):
    if message.author.guild_permissions.administrator:
        await bot.ban(member, days)
    else:
        await bot.say("権限確認してください")
@bot.event
async def on_message(message):
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('消すぞーー')
        else:
            await message.channel.send('は？おめーには権限ねーよ||殺||すぞ')
#@bot.command(pass_context=True)
#async def kick(ctx, user_name: discord.User):
#    if message.author.guild_permissions.administrator:
#        await bot.kick(member, days)
#    else:
#        await bot.say("権限ねーよKS")
bot.run("NTc5NTg4NTQ4Mjc4MDkxNzk4.XPEF8g.kduskv79DFuzB7dTC2kqVhNrvl4")

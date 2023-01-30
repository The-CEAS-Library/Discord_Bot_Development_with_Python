import discord

# Assign the client variable to the result of discord.Client().
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

# Define an async function under the client event parameter.
# This function will print the bot user's client ID to our console
# once the async function has returned that we have logged in sucessfully.
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

guild_ids = ['guild_id']

# ping -- returns message "Pong!" to check the bot's online status.
@bot.slash_command(guild_ids=guild_ids)
async def ping(ctx):
    await ctx.respond('Pong!')

# hello - will return the string "Hello, user!" depending on user.
@bot.slash_command(guild_ids=guild_ids)
async def hello(ctx):
    await ctx.respond('Hello!')

# aboutme - will return the name and the pfp image of the user in an embed
@bot.slash_command(guild_ids=guild_ids)
async def aboutme(ctx):
    print(ctx)
    embed=discord.Embed(title=ctx.author.name)
    embed.set_thumbnail(url=ctx.author.avatar.url)
    await ctx.respond(embed=embed)

# help -- will direct message the user a help message.
@bot.slash_command(guild_ids=guild_ids)
async def help(ctx, cmd):
    if cmd == 'help':
        await ctx.respond('this message')
    elif cmd == 'hello':
        await ctx.respond('replies \'hello\' to your command')
    elif cmd == 'ping':
        await ctx.respond('replies \'Pong!\' to your command')
    elif cmd == 'aboutme':
        await ctx.respond('shows info about the user')
    else:
        await ctx.respond('command does not exist')

# good bot
@bot.event
async def on_message(message):
    # print(message)
    if message.content.lower() == 'good bot':
        await message.add_reaction('❤️')

# This line assigns our client with the correct bot token, authenticating
# that we have access to run our code on this bot user.
bot.run('bot_token')
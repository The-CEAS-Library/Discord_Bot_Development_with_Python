from discord.ext import commands
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


# ping -- returns message "Pong!" to check the bot's online status.
@bot.slash_command(name="ping", description="Ping the bot")
async def ping(ctx):
    await ctx.respond('Pong!')

# hello - will return the string "Hello, user!" depending on user.
@bot.slash_command(name="hello")
async def hello(ctx):
    await ctx.respond('Hello User!')
    

#aboutme - will return the name and the pfp image of the user in an embed
@bot.slash_command(name="about-me")
async def aboutme(ctx):
    embed=discord.Embed(title=ctx.user.display_name)
    embed.set_thumbnail(url=ctx.user.display_avatar)
    await ctx.respond(embed=embed)

# help -- will direct message the user a help message.
@bot.slash_command(name="help", description='Type in the command that you want to know more about')
async def help(ctx, cmd):
    commands = {
        'ping': ' is to check if the bot is online or not',
        'hello': ' is to say hello to the bot',
        'help': ' is to get help with the bot'
    }
    await ctx.send(cmd.upper() + commands[cmd])
    
# good bot
@bot.event
async def on_message(message):
    if message.content.lower() == 'good bot':
      print('we re bt to run sth')
      await message.add_reaction('💖')

# This line assigns our client with the correct bot token, authenticating
# that we have access to run our code on this bot user. To do this, we just simply need to 
# retrieve the token we store in the env
bot.run(DISCORD_TOKEN)
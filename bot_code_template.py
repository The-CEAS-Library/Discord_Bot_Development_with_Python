from discord.ext import commands
import discord
import datetime

# Assign the client variable to the result of discord.Client().
intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot()

# Define an async function under the client event parameter.
# This function will print the bot user's client ID to our console
# once the async function has returned that we have logged in sucessfully.
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    

@bot.slash_command(name="ping", description="Ping the bot")
async def ping(ctx):
    await ctx.respond('pong')

@bot.slash_command(name="today", description="Command the bot to tell you the date")
async def today(ctx):
    today = datetime.date.today()
    await ctx.send(today)


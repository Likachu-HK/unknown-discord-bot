import interactions
import discord
import os
from time import sleep as wait
from discord.ext import tasks

bot = interactions.Client(token=os.getenv("TOKEN"))

client = discord.Client()
message = discord.Message

@bot.command(
    name="say",
    description="say something!",
    options = [
        interactions.Option(
            name="content",
            description="What you want to say",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def say(ctx: interactions.CommandContext, text: str):
    await ctx.send(f"{text}")

@bot.command(
    name="spam",
    description="Spam A Message every 7 seconds.",
)
async def spam(ctx: interactions.CommandContext):
    txt = {text}
    rep.start()
    await ctx.send(f"Started!")

@bot.command(
    name="stop"
    description="Stop the spamming"
)
async def stop(ctx: interactions.CommandContext):
     rep.stop()
     await ctx.send("Stopped."
@tasks.loop(seconds=7)
async def rep():
      await message.channel.send("<@897858526662258749>")

bot.start()

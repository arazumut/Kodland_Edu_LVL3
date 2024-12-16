import discord
from discord.ext import commands
from commands import add_task, delete_task, show_tasks, complete_task
from database import init_db

# Produced By K.Umut Araz

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı.")
    init_db()

@bot.command()
async def add_task(ctx, *, description):
    message = add_task(description)
    await ctx.send(message)

@bot.command()
async def delete_task(ctx, task_id: int):
    message = delete_task(task_id)
    await ctx.send(message)

@bot.command()
async def show_tasks(ctx):
    message = show_tasks()
    await ctx.send(message)

@bot.command()
async def complete_task(ctx, task_id: int):
    message = complete_task(task_id)
    await ctx.send(message)

# Bot tokeninizi buraya girin
bot.run("Your Bot Token")

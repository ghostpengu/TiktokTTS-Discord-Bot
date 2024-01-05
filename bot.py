from discord.ext import commands
import discord
import random
from discord import app_commands
from discord.ext.commands import Bot, has_permissions, CheckFailure
from tiktoktts import *
from server import *
intents = discord.Intents.all()
intents.message_content = True
import threading
import os
bot = commands.Bot(command_prefix='!',intents= discord.Intents.all())


files = os.listdir("out/") 

        # Iterate through the files and delete them
for file in files:
    file_path = os.path.join("out/", file)
    if os.path.isfile(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
@bot.event
async def on_ready():
    activity = discord.Game(name="Sad life😥", type=3)
    await bot   .change_presence(activity=discord.Game(name="Sad life😥", type=2))
    try:
        sync = await bot.tree.sync()
        print(f"Synced {len(sync)}")
    except Exception as e:
        print(e)
    print("loged as {0.user}".format(bot))

#25mb
token = "YOUR TOKEN HERE"
@bot.command(pass_context=True)
async def generate_audio(ctx,*,text: str):
    tts("e8deeb147d7ae7a7dacb88bf15e78e0b",req_text=text)
    await ctx.send(file=discord.File(r'voice.mp3'))
videos = []
@bot.command(pass_context=True)
async def generate(ctx,*,text: str):
    
    path = gen(text,"YOUR SESSION ID HERE")
    if os.path.getsize(path) < 25000000:
        await ctx.send(file=discord.File(path))
    else:


        embed = discord.Embed(title=f"Done!! {ctx.message.author}",
                            description=f"Download link is ready: http://"YOUR IP HERE":5000/download?file={path} ",
                            colour=0x1df500)
        videos.append(f"out/{path}")

        
        
        await ctx.send(embed=embed)
flask_thread = threading.Thread(target=run)

# Start Flask thread
flask_thread.start()
bot.run(token=token)

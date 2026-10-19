import os
import discord
from discord.ext import commands, tasks
import datetime

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# 1. ÄNDRA TILL DITT KANAL-ID HÄR (ta bort fnuttarna runt siffrorna)
CHANNEL_ID = 1561668604829769798  

@bot.event
async def on_ready():
    print(f'Bot online {bot.user}')
    boss_timer_loop.start()

@tasks.loop(seconds=60)
async def boss_timer_loop():
    now = datetime.datetime.now()

    if now.minute == 20:
        channel = bot.get_channel(int(CHANNEL_ID))
        if not channel:
            return

        if now.hour % 2 == 0:
            await channel.send("⚔️ **Boss Spawn :** Junichiro and The Parasite has spawned.")
        else:
            await channel.send("⚔️ **Boss Spawn :** Nivis and The Masked Warrior has spawned.")

# 2. ÄNDRA TILL DIN HEMLIGA TOKEN HÄR (behåll fnuttarna kvar runt texten)
bot.run(os.environ.get("DISCORD_TOKEN")

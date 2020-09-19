@client.event
async def on_ready():
    activity = discord.Game(name="!yardım")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot çalışıyor.")

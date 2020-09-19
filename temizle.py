@client.command(pass_context=True)
@commands.has_permissions(manage_messages=True) 
async def temizle(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount):
              messages.append(message)
    await channel.delete_messages(messages)
    await ctx.send('Mesaj silindi.', delete_after=2)

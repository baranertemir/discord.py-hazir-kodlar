@client.command()
@commands.has_permissions(administrator=True)
async def tekme(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

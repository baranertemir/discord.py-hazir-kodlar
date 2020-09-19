@client.command()
@commands.has_permissions(administrator=True)
async def yasakla(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Sunucudan yasaklandı {member.mention}')

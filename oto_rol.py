@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "rol") 
    await ctx.add_roles(role)

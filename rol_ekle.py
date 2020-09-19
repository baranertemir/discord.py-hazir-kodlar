@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def rolekle(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"{ctx.author.name}, {user.name} isimli üyeye bir rol verdi: {role.name}")

@client.command()
async def botaciklama(ctx):
    embed = discord.Embed(title="Yapımcı", description="A.Baran Ertemir") #,color=Hex code
    embed.set_author(name="A.Baran Ertemir")
    embed.add_field(name="Amacı", value="Deneme")
    embed.set_image(url="https://blog.loomly.com/wp-content/uploads/2019/06/earth.gif")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def yardim(ctx):
    author = ctx.message.author
    embed = discord.Embed(colour=discord.Colour.blue())
    
    embed.set_author(name="Yardım")
    embed.add_field(name=".botaciklama", value="Bot hakkında bilgiler verir.", inline=False)
    embed.add_field(name=".temizle", value="Mesaj temizlemeye yarar. Yanına istediğiniz değeri girerek o sayıda mesaj silmesini sağlayabilirsiniz. Örnek: .temizle 15", inline=False)
    
    await author.send(embed=embed)

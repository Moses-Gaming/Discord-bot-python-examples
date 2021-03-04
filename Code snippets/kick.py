@client.command(name='kick', pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(context, member: discord.Member):
  
  await member.kick()
  await context.send('user ' + member.display_name + ' has been kicked.')

@client.command(name='ban', pass_context = True)
@commands.has_permissions(kick_members=True)
async def ban(context, member: discord.Member, *, reason=None):
  
  await member.ban(reason=reason)
  await context.send('user ' + member.display_name + ' has been banned.')

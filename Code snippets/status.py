@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('YOUR STATUS HERE'))


def tagall(message):
    try:
        space = '\n\n'
        members = message.guild.members
        for member in members:
            mention = member.mention
            space ='🔰 '+ mention +'\n\n' +  space
        return space
    except:
        return 'Error in tag command.. \n Contact Developer'



import requests
import os
import discord
from plugin import quote
from alive import alive
from menu import menus
from update import reloads
import config
from plugin import random_img
from plugin import color
from plugin import google
from plugin import cmd
from plugin import status






# config names
_google = cmd.cmd['google']
_quote = cmd.cmd['quote']
_alive = cmd.cmd['alive']
_list = cmd.cmd['list']
_update = cmd.cmd['update']
_pic = cmd.cmd['ran_pic']
_clear = cmd.cmd['clear']

_error = cmd.msgs['error']
_errorMsg = cmd.msgs['error_msg']
_active = cmd.msgs['active']
_dev = cmd.msgs['dev']

_BotName = config.config['bot_name']
_ChannelId = config.config['channel_id']
_AliveMsg = config.config['alive_msg']
_MenuName = config.config['menu_name']


# engin

t_key = config.config['TOKEN']


#intents = discord.Intents(messages=True, guilds=True)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print(_active)
    print(_dev)
    channel_id = int(_ChannelId)
    channel = client.get_channel(channel_id)
    embed = discord.Embed(title="Online", description='Bot is online', color=color.emcolor())

    if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.DMChannel):     
        await channel.send(embed=embed)
    else:
        print("The channel is not a TextChannel or DMChannel")
    application = await client.application_info()
    owner = application.owner
    embed = discord.Embed(title="Online", description='Bot is online', color=color.emcolor())
    await owner.send(embed=embed)
    embed = discord.Embed(title=_MenuName, description=menus(), color=color.emcolor())
    await owner.send(embed=embed)
    #print(f"Owner ID: {owner.id}")



@client.event
async def on_message(message):
    if message.author == client.user:
        return



# random quote generate

    if message.content.startswith(_quote):
      try:
        embed = discord.Embed(title="Quote", description=quote.quote(), color=color.emcolor())
        imgs = random_img.random_img()
        embed.set_image(url=imgs)
        await message.channel.send(embed=embed)

      except:
         embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
         await message.channel.send(embed=embed)
         



# alive message

    if message.content.startswith(_alive):
      embed = discord.Embed(title=_AliveMsg, description=_BotName, color=color.emcolor())
      imgs = config.config['pic_url']
      embed.set_image(url=imgs)
      await message.channel.send(embed=embed)





#list
    if message.content.startswith(_list):
      try:
        embed = discord.Embed(title=_MenuName, description=menus(), color=color.emcolor())
        await message.channel.send(embed=embed)
      except:     
            embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
            await message.channel.send(embed=embed)
          







#update

    if message.content.startswith(_update):
      try:
        embed = discord.Embed(title="Update....", description='Restarting....♻', color=color.emcolor())
        await message.channel.send(embed=embed)
        await reloads(message)
      except:
            embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
            await message.channel.send(embed=embed) 

#down server
    if message.content.startswith('.logout'):
          embed = discord.Embed(title="Shutdown", description='Have a nice day', color=color.emcolor())
          await message.channel.send(embed=embed)
          await client.close()


              





# random picture generate
    if message.content.startswith(_pic):
      try:
        url = random_img.random_img()
        embed = discord.Embed()
        embed.set_image(url=url)
        embed.description = f'Random Picture by {_BotName}'
        await message.channel.send(embed=embed)

      except:
              embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
              await message.channel.send(embed=embed)         





    if message.content == '!embed':
        embed = discord.Embed(title="Embed Title", description="Embed Description", color=color.emcolor())
        embed.set_image(url='https://i.imgur.com/wSTFkRM.png')
        await message.channel.send(embed=embed)







#google serch engine

    if message.content.startswith(_google):

      try:
          url_str = google.google(message)
          embed = discord.Embed(title=f"{_BotName} Search Engine", description=url_str, color=color.emcolor())
          await message.channel.send(embed=embed)

      except:
          embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
          await message.channel.send(embed=embed)






#chat clear
    if message.content == _clear:
        try:          
          if message.author.guild_permissions.manage_messages:
              deleted = await message.channel.purge(limit=10)
              embed = discord.Embed(title=f"{_BotName} Clear", description=f'Deleted {len(deleted)} messages.', color=color.emcolor())
              await message.channel.send(embed=embed)
          else:
              embed = discord.Embed(title=_error, description='You do not have permission to use this command.', color=color.emcolor())
              await message.channel.send(embed=embed)

        except Exception as e:          
                embed = discord.Embed(title= _error, description='This command work only in the channel', color=color.emcolor())
                await message.channel.send(embed=embed)
            

#server status
    if message.content == '.status':
        try:
          await message.channel.send(embed=status.status(message))

        except:
            embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
            await message.channel.send(embed=embed)
            



      
      
      
#alive()
client.run(t_key)


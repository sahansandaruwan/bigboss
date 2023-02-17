
import requests
import os
import discord
from plugin import quote
from cloud import alive
from menu import menus
from update import reloads
import config
from plugin import random_img
from plugin import color
from plugin import google
from plugin import cmd
from plugin import status
from plugin import textsty
from plugin import spam
from plugin import youtube
from plugin import tagall




if os.environ['Deploy'] == 'yep':
  _BotName = os.environ['Bot_Name']
  _ChannelId = os.environ['Channel_ID']
  _AliveMsg = os.environ['Alive_msg']
  _MenuName = os.environ['Menu_Name']
  _Tkey = os.environ['TOKEN']
  _AliveImg = os.environ['pic_url']
else:
  _BotName = config.config['bot_name']
  _ChannelId = config.config['channel_id']
  _AliveMsg = config.config['alive_msg']
  _MenuName = config.config['menu_name']
  _Tkey = config.config['TOKEN']
  _AliveImg = config.config['pic_url']

   




   
   












# config names
_google = cmd.cmd['google']
_quote = cmd.cmd['quote']
_alive = cmd.cmd['alive']
_list = cmd.cmd['list']
_restart = cmd.cmd['restart']
_pic = cmd.cmd['ran_pic']
_clear = cmd.cmd['clear']

_error = cmd.msgs['error']
_errorMsg = cmd.msgs['error_msg']
_active = cmd.msgs['active']
_dev = cmd.msgs['dev']




#intents = discord.Intents(messages=True, guilds=True)
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    color.printbanner()
    print(f'We have logged in as {client.user}')
    print(_active)
    print(_dev)  
    try:    
      channel_id = int(_ChannelId)
      channel = client.get_channel(channel_id)
      embed = discord.Embed(title="Online", description='Bot is online', color=color.emcolor())
      if isinstance(channel, discord.TextChannel) or isinstance(channel, discord.DMChannel):     
          await channel.send(embed=embed)
      else:
          print("The channel is not a TextChannel or DMChannel")
    except:
        print('Enter Channel id')
    application = await client.application_info()
    owner = application.owner
    embed = discord.Embed(title="Online", description='Bot is online', color=color.emcolor())
    await owner.send(embed=embed)
    embed = discord.Embed(title=_MenuName, description=menus(), color=color.emcolor())
    await owner.send(embed=embed)


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
      imgs = _AliveImg
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
          







#restart

    if message.content.startswith(_restart):
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
            embed = discord.Embed(title= _error, description= 'This command work only in the channel', color=color.emcolor())
            await message.channel.send(embed=embed)

#developer info
    if message.content == '.dev':
        try:
            url = cmd.dev['img_url']
            embed = discord.Embed()
            embed.set_image(url=url)
            embed.title = 'Developer Info'
            embed.description = f'**Name:  **Sahan Sandaruwan \n **Web:  ** https://sahansandaruwan.pages.dev \n **GitHub URL: ** https://github.com/sahansandaruwan \n **Repo URL: **https://github.com/sahansandaruwan/bigboss'
            await message.channel.send(embed=embed)
            
        except:
           embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
           await message.channel.send(embed=embed)    



#spam message
    if message.content.startswith('.textspam'):
        try:
          num = spam.textspam(message)
          for i in range(num):
            await message.channel.send(f'spam number {i}')
        except:
          embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
          await message.channel.send(embed=embed)              


#text markup menu
    if message.content == '.textmark':
        try:
            embed = discord.Embed(title=f"{_BotName} Discord Text Markdown", description=textsty.textstylemenu(), color=color.emcolor())
            await message.channel.send(embed=embed)
        except:
          embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
          await message.channel.send(embed=embed)  

    
#text markup engin 
    if message.content.startswith('.bold'):
       textbold = textsty.textbold(message)
       embed = discord.Embed(title=f"{_BotName} Text Bold", description=textbold, color=color.emcolor())
       await message.channel.send(embed=embed) 

    if message.content.startswith('.italic'):
       TextItalic = textsty.TextItalics(message)
       embed = discord.Embed(title=f"{_BotName} Text Italics", description=TextItalic, color=color.emcolor())
       await message.channel.send(embed=embed)

    if message.content.startswith('.botalic'):
       BoldItalic = textsty.BoldItalics(message)
       embed = discord.Embed(title=f"{_BotName} Bold Italics", description=BoldItalic, color=color.emcolor())
       await message.channel.send(embed=embed)
    
    if message.content.startswith('.underline'):
       TextUnderlin = textsty.TextUnderline(message)
       embed = discord.Embed(title=f"{_BotName} Text Underline", description=TextUnderlin, color=color.emcolor())
       await message.channel.send(embed=embed)

    if message.content.startswith('.codeblock'):
       CodeBloc = textsty.CodeBlocks(message)
       embed = discord.Embed(title=f"{_BotName} Code Blocks", description=CodeBloc, color=color.emcolor())
       await message.channel.send(embed=embed)

    if message.content.startswith('.strike'):
       Strikethroug = textsty.Strikethrough(message)
       embed = discord.Embed(title=f"{_BotName} Strikethrough", description=Strikethroug, color=color.emcolor())
       await message.channel.send(embed=embed)

    if message.content.startswith('.unbolic'):
       UnderlineBoldItalic = textsty.UnderlineBoldItalics(message)
       embed = discord.Embed(title=f"{_BotName} Underline Bold Italics", description=UnderlineBoldItalic, color=color.emcolor())
       await message.channel.send(embed=embed)
    
    if message.content.startswith('.blockquote'):
       BlockQuote = textsty.BlockQuotes(message)
       embed = discord.Embed(title=f"{_BotName} Block Quotes", description=BlockQuote, color=color.emcolor())
       await message.channel.send(embed=embed)

#youtube search engin
    if message.content.startswith('.yt'):
      try:
          msg = youtube.ytsearch(message)
          embed = discord.Embed(title=f"{_BotName} Youtube Search Engine", description=msg, color=color.emcolor())
          await message.channel.send(embed=embed)

      except:
          embed = discord.Embed(title= _error, description= _errorMsg, color=color.emcolor())
          await message.channel.send(embed=embed)

    if message.content.startswith('.tagall'):
            tag = tagall.tagall(message)
            embed = discord.Embed(title=f"{_BotName} Tag", description=tag, color=color.emcolor())
            await message.channel.send(embed=embed)
             



    
      
       



            



            
        
        
            
                 

            

            



           
      
alive()

client.run(_Tkey)

   


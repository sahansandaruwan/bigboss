import discord
import datetime
from plugin import color

def status(message):
        
        guild = message.guild
        online_members = len([m for m in guild.members if m.status == discord.Status.online])
        total_members = len(guild.members)
        uptime = datetime.datetime.now(datetime.timezone.utc) - guild.created_at
        uptime_formatted = str(uptime).split(".")[0]
        embed = discord.Embed(title=f'Server Statistics for {guild.name}', color=color.emcolor())
        embed.add_field(name="Total Members", value=total_members)
        embed.add_field(name="Online Members", value=online_members)
        embed.add_field(name="Server Uptime", value=uptime_formatted)
        return embed





#000000: Black
#FFFFFF: White
#FF0000: Red
#00FF00: Lime
#0000FF: Blue
#FFFF00: Yellow
#00FFFF: Cyan
#FF00FF: Magenta
#808080: Gray
#C0C0C0: Silver
#800000: Maroon
#008000: Green
#000080: Navy
#808000: Olive
#008080: Teal
#800080: Purple

import random
import discord

color  = ["#000000", "#FFFFFF", "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#00FFFF", "#FF00FF", "#808080", "#C0C0C0", "#800000", "#008000", "#000080", "#808000", "#008080", "#800080"]

def emcolor():
    colorcode = random.choice(color)
    color_object = discord.Color(int(colorcode[1:], 16))
    return color_object


emcolor()
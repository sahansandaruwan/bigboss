import os
import discord
import sys


async def reloads(message):
    os.execl(sys.executable, sys.executable, *sys.argv)
  
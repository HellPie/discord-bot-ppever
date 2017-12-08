from discord.ext import commands
import discord

__version__ = '0.1'


class PPEverBot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix=None)

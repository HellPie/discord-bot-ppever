import logging

from discord.ext import commands
import discord

__title__ = '++Ever Bot'
__description__ = 'Joke bot made for the Vainglory API official unofficial Discord guild'
__author__ = '_HellPie'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright (c) 2017 Diego Rossi'
__version__ = '0.1'

_initial_extensions = ()


def _prefix_handler(bot: commands.Bot, msg: discord.Message):
	prefixes = [f'<@!{bot.user.id}>', f'<@{bot.user.id}>']
	if msg.guild is not None:
		prefixes.append(f'{msg.guild.display_name}, ')
	return prefixes


class PPEverBot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix=_prefix_handler, description=__description__)
		self.log = logging.Logger(__name__)
		for extension in _initial_extensions:
			try:
				self.load_extension(extension)
			except (discord.ClientException, ImportError) as e:
				self.log.error(f'INIT: {extension}: {e}')
	
	async def on_ready(self):
		self.log.info(f'ON_READY: {self.user.name} - ID: {self.user.id}')
	
	async def on_command_error(self, context: commands.Context, exception: Exception):
		self.log.error(f'ON_ERROR: {context.author.name}@{context.channel.name}@{context.guild.name}: {exception}')

import discord
from discord.ext import commands

__title__ = '++Ever Bot'
__description__ = 'Joke bot made for the Vainglory API official unofficial Discord guild'
__author__ = '_HellPie'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright (c) 2017 Diego Rossi'
__version__ = '0.1'

_initial_extensions = (
	'extensions.rename',
)


def _prefix_handler(bot: commands.Bot, msg: discord.Message):
	prefixes = [f'<@!{bot.user.id}> ', f'<@{bot.user.id}> ']
	if msg.guild is not None:
		prefixes.append(f'{msg.guild.me.display_name}, ')
	return prefixes


class PPEverBot(commands.Bot):
	def __init__(self):
		super().__init__(
			command_prefix=_prefix_handler,
			description=__description__,
			game=discord.Game(name='4ever sleep', type=3)
		)
		for extension in _initial_extensions:
			try:
				self.load_extension(extension)
			except Exception as e:
				print(f'INIT: {extension}: {e}')
	
	async def on_ready(self):
		print(f'INF: ON_READY: {self.user.name} - ID: {self.user.id}')
	
	async def on_command_error(self, context: commands.Context, exception: Exception):
		print(f'ERR: ON_ERROR: {context.author.name}@{context.channel.name}@{context.guild.name}: {exception}')

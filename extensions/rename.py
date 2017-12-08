import re
import json

import discord
from discord.ext import commands


class Rename:
	"""Automated nickname update functionality."""
	
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.settings = {
			'count': 0
		}
		try:
			settings = open('settings/rename.json')
			self.settings = json.load(settings)
			settings.close()
		except FileNotFoundError:
			self.update_settings({})
	
	async def __local_check(self, ctx: commands.Context) -> bool:
		return await self.bot.is_owner(ctx.author)
	
	@commands.command(pass_context=True, name='count')
	async def set_counter(self, ctx: commands.Context, *, count: int):
		"""Set a base number to start counting from."""
		
		self.update_settings(settings={'count': count})
		return await ctx.send(
			embed=discord.Embed(
				description=f'Now counting from {self.settings["count"]}.',
				colour=0x8E44AD
			).set_author(
				name=self.bot.user.name,
				icon_url=self.bot.user.avatar_url
			).set_footer(
				text=f'Made by @{self.bot.get_user(self.bot.owner_id).name} with \N{BLACK HEART SUIT}',
				icon_url=self.bot.get_user(self.bot.owner_id).avatar_url
			)
		)
	
	async def on_message(self, msg: discord.Message):
		if msg.author.bot:
			return
		if re.search(r'\d+ever|<@!?99755417541828608>', msg.content):
			self.update_settings({'count': self.settings["count"] + 1})
			try:
				await msg.guild.get_member(99755417541828608).edit(nick=f'{self.settings["count"]}ever')
			except Exception as e:
				print(f'ERR: SET_NICK: {e}')
			if self.settings["count"] == 100:
				try:
					await msg.add_reaction('\N{HUNDRED POINTS SYMBOL}')
				except Exception as e:
					print(f'ERR: ADD_EMOTE: {e}')
	
	def update_settings(self, settings: dict):
		if settings is not None or settings != {}:
			self.settings.update(settings)
			with open('storage/rename.json', 'w') as rename_json:
				json.dump(self.settings, rename_json)


def setup(bot: commands.Bot):
	bot.add_cog(Rename(bot))

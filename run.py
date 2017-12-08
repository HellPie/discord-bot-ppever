import os
import argparse
import configparser
import bot


def run():
	args_parser = argparse.ArgumentParser(
		description='Joke bot made for the Vainglory API official unofficial Discord guild',
		epilog='Made with <3 by @_HellPie#9429',
		add_help=False
	)
	args_parser.add_argument(
		'-h', '--help',
		action='help',
		help='Shows this help message and exits.'
	)
	args_parser.add_argument(
		'-v', '--version',
		action='version',
		help='Shows the version of this Bot and exits.',
		version=f'++Ever v{bot.__version__}'
	)
	args_parser.add_argument(
		'-c', '--conf',
		default='config.ini',
		help='Start the Bot using the specified config file. (Defaults to \'config.ini\')',
		metavar='FILE',
		dest='config_file'
	)
	arguments = args_parser.parse_args()
	if not hasattr(arguments, 'config_file'):
		print('No configuration file specified. See \'-h\' for help.')
		exit(1)
	config_parser = configparser.ConfigParser()
	config_parser.read(arguments.config_file)
	token = config_parser.get(section='DISCORD', option='TOKEN', fallback=str())
	if token is None or token == str() or token.isspace():
		print('Unable to read Discord Bot token. Check your config file.')
		exit(1)
	if 'storage' not in os.listdir('.'):
		os.mkdir('storage')
	if 'storage' not in os.listdir('.'):
		print('Unable to configure necessary \'storage\' directory. Check folder and script permissions.')
		exit(1)
	bot.PPEverBot().run(token)


if __name__ == '__main__':
	run()

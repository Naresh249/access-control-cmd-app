import argparse

from conf import db_connection as db_conn
from conf import constants as const
from resources.utils import * 

def execute_command(cmd_name):
	"""
	Executing Command Provided by User
	"""
	if cmd_name not in const.COMMANDS.values():
		return {
			'status': False, 
			'error': 'Invalid Command Line!'}
	success_response = eval(const.COMMAND_EXECUTION.get(cmd_name))
	return success_response

if __name__ == '__main__':
	db_connection = db_conn.InitDbConnection()
	parser = argparse.ArgumentParser(
			prog='Role Based Access System',
			usage='Usage: Pass the Command To Access the Features',
			description=const.DESCRIPTION,
			epilog='Copyrights @Naresh Yadav | 8123961170',
			add_help=True)
	parser.add_argument(
		"cmd_name", type=str,
		metavar="Regitser User --> regu\n  Add Role --> addrole")
	cmd_name = parser.parse_args().cmd_name
	res = execute_command(cmd_name)
	print(res)





import argparse

from conf import db_connection as db_conn
from conf import constants as const

if __name__ == '__main__':
	db_connection = db_conn.InitDbConnection()
	parser = argparse.ArgumentParser(
			prog='Role Based Access System',
			usage='Usage: Pass the Command To Access the Features',
			description=const.DESCRIPTION,
			epilog='Copyrights @Naresh Yadav | 8123961170',
			add_help=True)
	parser.add_argument(
		"cmd_name", type=str, help='Enter the Command Name First Available Command Can be seen in help',
		metavar="CMD NAME")
	args = parser.parse_args()







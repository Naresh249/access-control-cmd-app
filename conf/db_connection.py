import sqlite3
from conf import db_queries as db_query

DATABASE_NAME = "acs.db"

class InitDbConnection():
	"""
	Initializing Database connection
	"""
	def __init__(self):
		"""
		Setting Inital models in Memory if not exists
		"""
		# conn = sqlite3.connect(":memory:")
		conn = sqlite3.connect(DATABASE_NAME)
		conn.execute(db_query.CREATE_USER_TABLE)
		conn.execute(db_query.CREATE_ROLE_TABLE)
		conn.execute(db_query.CREATE_USER_ROLE_TABLE)
		conn.execute(db_query.CREATE_RESOURCES_TABLE)
		conn.execute(db_query.CREATE_RESOURCES_ACCESS_TABLE)
		conn.execute(db_query.CREATE_ADMIN_USER_MAPPING)

	def open_connection(self):
		"""
		Opening Database Connection
		"""
		conn = sqlite3.connect(DATABASE_NAME)
		return conn
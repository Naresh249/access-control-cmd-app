import datetime
import json

from resources import request_validators as req_validators
from conf import db_connection as db_conn
from conf import db_queries as db_query


def register_user():
	"""
	Registering User as Admin in the system
	"""
	params = input('Provide User Details in Json Format Example\n'\
					'{"name": "Naresh", "email": "nky249@gmail.com", "password": "123"}\n')
	try:
		params = json.loads(params)
		request_validator = req_validators.validate_register_user_params(params)
		if not request_validator.get('status'):
			return request_validator
		# Registering User Here
		conn_init = db_conn.InitDbConnection()
		conn = conn_init.open_connection()
		cr = conn.cursor()
		cr.execute(
			db_query.INSER_RECORD_QUERY.format(
				table_name='user',
				col_name=db_query.USER_COL_NAME,
				values=(
					params.get('name'),
					params.get('email'),
					params.get('password'),
					params.get('mobile', ''),
					'True')))
		conn.commit()
		conn.close()
		return {'status': True, 'message': 'Sucessfully Created User!'}
	except Exception as e:
		return {'status': False, 'error': 'Invalid Request Format.' + str(e)}

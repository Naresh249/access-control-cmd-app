import re

from conf import db_connection as db_conn

def validate_register_user_params(params):
	"""
	Validating Register User Params
	"""
	# Try Catch validates for the required Fields
	try:
		name = params['name'],
		email = params['email'],
		password = params['password']
	except Exception as e:
		return {
			'status': False, 
			'error': 'Field Required {}'.format(str(e))}
	# Validation Email
	req = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
	if not req.match(params.get('email')):
		return {'status': False, 'error': 'Provide Vaild Email Id.'}

	conn_init = db_conn.InitDbConnection()
	conn = conn_init.open_connection()
	cr = conn.cursor()
	if cr.execute(
		"select * from user where email = '{email}'".format(
			email=params.get('email'))).fetchall():
		return {'status': False, 'error': 'Email Already Exists!'}
	return {'status': True}


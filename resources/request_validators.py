import json
import re

from conf import db_connection as db_conn

def get_valid_user_details(user_password_params):
	"""
	Validating the Users
	"""

	try:
		user_password_params = json.loads(user_password_params)
		email = user_password_params['email']
		password = user_password_params['password']
	except Exception as e:
		return {
			'status': False, 
			'error': 'Field Required {}'.format(str(e))}
	conn_init = db_conn.InitDbConnection()
	conn = conn_init.open_connection()
	cr = conn.cursor()
	user_details = cr.execute(
		"select * from user where email = '{email}' and password = '{password}'".format(email=user_password_params.get('email'), password=user_password_params.get('password'))).fetchone()
	if not user_details:
		return {'status': False, 'error': 'Invalid Credentails.'}
	return {'status': True, 'data': user_details}

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

def validate_add_role_params(params):
	"""Validating Role Params"""
	try:
		role=params['role']
	except Exception as e:
		return {
			'status': False, 
			'error': 'Field Required {}'.format(str(e))}

	if params.get('is_readable') and type(params.get('is_readable')) != bool:
		return {
			'status': False, 
			'error': 'is_readable is required in Boolean Data.'}

	if params.get('is_writable') and type(params.get('is_writable')) != bool:
		return {
			'status': False, 
			'error': 'is_writable is required in Boolean Data.'}

	if params.get('is_deletable') and type(params.get('is_deletable')) != bool:
		return {
			'status': False, 
			'error': 'is_deletable is required in Boolean Data.'}
	
	user_password = input('Enter Email and Password In JSON Format i.e - {"email": "nky249@gmail.com", "password": "XXXX"}\n')
	user_details = get_valid_user_details(user_password)
	if not user_details.get('status'):
		return user_details
	params['created_by_id'] = user_details.get('data')[0]
	return {"status": True, "params": params}
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
			db_query.INSERT_RECORD_QUERY.format(
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

def add_role():
	"""
	Adding Role 
	"""
	params = input('Provide Role Details in Json Format Example\n'\
					'{"role": "Commiter", "is_readable": true, "is_writable": false, "is_deletable": true}\n')
	try:
		params = json.loads(params)
		request_validator = req_validators.validate_add_role_params(params)
		if not request_validator.get('status'):
			return request_validator
		conn_init = db_conn.InitDbConnection()
		conn = conn_init.open_connection()
		cr = conn.cursor()
		params = request_validator.get('params')
		cr.execute(
			db_query.INSERT_RECORD_QUERY.format(
				table_name='role',
				col_name=db_query.ROLE_COL,
				values=(
					params.get('role'),
					str(params.get('is_readable', False)),
					str(params.get('is_writable', False)),
					str(params.get('is_deletable', False)),
					params.get('created_by_id')
					)))
		conn.commit()
		conn.close()
		return {"status": True, "message":"Sucessfully Added Role"}
	except Exception as e:
		return {'status': False, 'error': 'Invalid Request Format, Expecting JSON.' + str(e)}		

def add_resources():
	"""
	Adding Resources
	"""
	params = input('Provide Resource Details in Json Format Example i .e\n {"resource_name": "Backend Repository", "description": "test"}\n')
	try:
		params = json.loads(params)
		request_validator = req_validators.validate_resource_request(params)
		if not request_validator.get('status'):
			return request_validator
		conn_init = db_conn.InitDbConnection()
		conn = conn_init.open_connection()
		cr = conn.cursor()
		params = request_validator.get('params')
		cr.execute(
			db_query.INSERT_RECORD_QUERY.format(
				table_name='resources',
				col_name=db_query.RESOURCE_COL,
				values=(
					params.get('resource_name'),
					params.get('description', ""),
					params.get('created_by_id')	
				)))
		conn.commit()
		conn.close()
		return {"status": True, "message":"Sucessfully Created Resouces"}
	except Exception as e:
		return {'status': False, 'error': 'Invalid Request Format, Expecting JSON.' + str(e)}

def assign_resource():
	"""
	Assigning Resources to User
	"""
	params = input('Provide Your Credentails i .e\n {"email": "nky249@gmail.com", "password": "XXX"}\n')
	user_details = req_validators.get_valid_user_details(params)
	if not user_details.get('status'):
		return user_details
	logged_in_user_id = user_details.get('data')[0]
	conn_init = db_conn.InitDbConnection()
	conn = conn_init.open_connection()
	cr = conn.cursor()
	resources = cr.execute('select id, resource_name from resources where created_by_id = {created_by_id}'.format(
		created_by_id=logged_in_user_id)).fetchall()
	if not resources:
		return {
			'status': False, 
			'message': 'No Resource Available For You, Create Resource by using CMD addresource'}
	users = cr.execute('select name, email from user').fetchall()
	role = cr.execute('select id, role from role where created_by_id = {}'.format(logged_in_user_id)).fetchall()
	assign_resource_user_params = input(
		'Provide Resources ID, Role ID and Email from Avialability i.e '\
		'"resource_id": 1, "role_id": 1, "email": "a@gmail.com"\n\n'\
		'Avaiable Resocues - {resources}\n'\
		'Available Roles - {role}\n'\
		'Available Users {users}\n'.format(
				resources=resources,
				role=role,
				users=users
			))
	try:
		params = json.loads(assign_resource_user_params)
	except Exception as e:
		return {'status': False, 'error': 'Need Json ' + str(e)}

	request_validator = req_validators.validate_assign_resources(
		params, logged_in_user_id)
	if not request_validator.get('status'):
		return request_validator
	# Assigning Resource
	cr.execute(
		db_query.INSERT_RECORD_QUERY.format(
			table_name='resourcesaccess',
			col_name=('resource_id', 'user_id'),
			values=(
				params.get('resource_id'),
				params.get('assign_user_id')	
			)))
	cr.execute(
		db_query.INSERT_RECORD_QUERY.format(
			table_name='userrole',
			col_name=('role_id', 'user_id'),
			values=(
				params.get('role_id'),
				params.get('assign_user_id')	
			)))
	conn.commit()
	return {"status": True, "message":"Sucessfully Assigned Resource and Role To User."}



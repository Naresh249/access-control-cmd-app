import json

def register_user():
	"""
	Registering User as Admin in the system
	"""
	params = input('Provide User Details in Json Format Example\n'\
					'{"name": "Naresh", "email": "nky249@gmail.com", "password": "123"}\n')
	try:
		params = json.loads(params)
	except Exception as e:
		return {'status': False, 'error': 'Invalid Request Format.'}

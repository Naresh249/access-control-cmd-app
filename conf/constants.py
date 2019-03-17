DESCRIPTION = """------Role Based Access System----------"""

COMMANDS = {
	'register_user': 'regu',
	'add_role': 'addrole',
	'add_resource': 'addresource',
	'assign_resource': 'assignresource'
}

COMMAND_EXECUTION = {
	COMMANDS['register_user']: 'register_user()',
	COMMANDS['add_role']: 'add_role()',
	COMMANDS['add_resource']:'add_resources()',
	COMMANDS['assign_resource']:'assign_resource()',
}
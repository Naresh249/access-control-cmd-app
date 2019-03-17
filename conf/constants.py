DESCRIPTION = """------Role Based Access System----------"""

COMMANDS = {
	'register_user': 'regu',
	'add_role': 'addrole',
	'add_resource': 'addresource',
	'assign_resource': 'assignresource',
	'read_resource': 'rread',
	'write_resource': 'rwrite',
	'delete_resource': 'rdelete',
}

COMMAND_EXECUTION = {
	COMMANDS['register_user']: 'register_user()',
	COMMANDS['add_role']: 'add_role()',
	COMMANDS['add_resource']:'add_resources()',
	COMMANDS['assign_resource']:'assign_resource()',
	COMMANDS['read_resource']:'read_resource()',
	COMMANDS['write_resource']:'write_resource()',
	COMMANDS['delete_resource']:'delete_resource()',
}
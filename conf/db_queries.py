COMMON_COLUMNS = """is_deleted boolean default false,"""\
				"""created_at datetime default current_timestamp,"""\
				"""updated_at datetime default current_timestamp"""

CREATE_USER_TABLE = """CREATE TABLE IF NOT EXISTS user("""\
					"""id integer PRIMARY KEY AUTOINCREMENT,"""\
					"""name text NOT NULL,"""\
					"""email text NOT NULL UNIQUE,"""\
					"""password text NOT NULL,"""\
					"""mobile_number text NULL,"""\
					"""{cmn_col},"""\
					"""is_admin boolean default false)""".format(cmn_col=COMMON_COLUMNS)

CREATE_ROLE_TABLE = """CREATE TABLE IF NOT EXISTS role("""\
					"""id integer PRIMARY KEY,"""\
					"""role text NOT NULL,"""\
					"""is_readable boolean default false,"""\
					"""is_writable boolean default false,"""\
					"""is_deletable boolean default false,"""\
					"""{cmn_col},"""\
					"""created_by_id integer NOT NULL,"""\
					"""FOREIGN KEY(created_by_id) REFERENCES user(id) ON DELETE CASCADE ON UPDATE NO ACTION)""".format(cmn_col=COMMON_COLUMNS)

CREATE_USER_ROLE_TABLE = """CREATE TABLE IF NOT EXISTS userrole("""\
						"""id integer PRIMARY KEY,"""\
						"""{cmn_col},"""\
						"""user_id integer NOT NULL,"""\
						"""role_id integer NOT NULL,"""\
						"""FOREIGN KEY (id) REFERENCES user (user_id) ON DELETE CASCADE ON UPDATE NO ACTION,"""\
						"""FOREIGN KEY (id) REFERENCES role (role_id) ON DELETE CASCADE ON UPDATE NO ACTION)""".format(cmn_col=COMMON_COLUMNS)

CREATE_RESOURCES_TABLE = """CREATE TABLE IF NOT EXISTS resources("""\
						"""id integer PRIMARY KEY,"""\
						"""resource_name text NOT NULL UNIQUE,"""\
						"""description text NULL,"""\
						"""{cmn_col},"""\
						"""created_by_id integer NOT NULL,"""\
						"""FOREIGN KEY (id) REFERENCES user (created_by_id) ON DELETE CASCADE ON UPDATE NO ACTION)""".format(cmn_col=COMMON_COLUMNS)

CREATE_RESOURCES_ACCESS_TABLE = """CREATE TABLE IF NOT EXISTS resourcesaccess("""\
							"""id integer PRIMARY KEY,"""\
							"""{cmn_col},"""\
							"""user_id integer NOT NULL,"""\
							"""resource_id integer NOT NULL,"""\
							"""FOREIGN KEY (id) REFERENCES user (user_id) ON DELETE CASCADE ON UPDATE NO ACTION,"""\
							"""FOREIGN KEY (id) REFERENCES resources (resource_id) ON DELETE CASCADE ON UPDATE NO ACTION)""".format(cmn_col=COMMON_COLUMNS)

CREATE_ADMIN_USER_MAPPING = """CREATE TABLE IF NOT EXISTS adminusermapping("""\
							"""id integer PRIMARY KEY,"""\
							"""{cmn_col},"""\
							"""admin_id integer NOT NULL,"""\
							"""member_id integer NOT NULL,"""\
							"""FOREIGN KEY (id) REFERENCES user (admin_id) ON DELETE CASCADE ON UPDATE NO ACTION,"""\
							"""FOREIGN KEY (id) REFERENCES user (member_id) ON DELETE CASCADE ON UPDATE NO ACTION)""".format(cmn_col=COMMON_COLUMNS)

SELECT_RECORD_QUERY = "SELECT * from {table_name} WHERE {where_clause}"

INSERT_RECORD_QUERY = "INSERT INTO {table_name} {col_name} VALUES {values}"

USER_COL_NAME = '(name, email, password, mobile_number, is_admin)'
ROLE_COL = '(role, is_readable, is_writable, is_deletable, created_by_id)'

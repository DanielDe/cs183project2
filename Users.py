import os
import re

class User:
	login = ""
	password = ""
	uid = ""
	gid = ""
	gecos = ""
	home = ""
	shell = ""

	def __init__(self):
		pass


class Users:
	users = {}

	def __init__(self, filename):
		# file input
		if os.path.exists(filename):
			lines = [line.rstrip('\n') for line in open(filename)]

			# building regex
			re_login = '(?P<login>[a-z]+)'
			re_password = '(?P<password>[*x])'
			re_uid = '(?P<uid>[0-9]+)'
			re_gid = '(?P<gid>[0-9]+)'
			re_gecos = '(?P<gecos>[a-zA-Z- ]*)'
			re_home = '(?P<home>(?:/[a-z]+)+)'
			re_shell = '(?P<shell>(?:/[a-z]+)+)'

			str_replace = [ re_login, re_password, re_uid,
											re_gid, re_gecos, re_home, re_shell ]
			re_string = '^%s:%s:%s:%s:%s:%s:%s$' % tuple(str_replace)

			for line in lines:
				matches = re.search(re_string, line)
				if matches:
					tempUser = User()
					tempUser.login = matches.group('login')
					tempUser.password = matches.group('password')
					tempUser.uid = matches.group('uid')
					tempUser.gid = matches.group('gid')
					tempUser.gecos = matches.group('gecos')
					tempUser.home = matches.group('home')
					tempUser.shell = matches.group('shell')
					self.users[tempUser.login] = tempUser

		else:
			raise ValueError('Could not find passwd file.')


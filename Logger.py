import datetime

class Logger:
	log_file = ""

	def print_info(self, script_name, result):
		output_str = "%s %s %s %s" % (datetime.datetime.now(), "INFO", script_name, result) 
		self.log(output_str)

	def print_warn(self, script_name, result):
		output_str = "%s %s %s %s" % (datetime.datetime.now(), "WARN", script_name, result) 
		self.log(output_str)

	def log(self, output):
		with open(self.log_file, "a") as appendFile:
			appendFile.write(output)


	def __init__(self):
		self.log_file = "./accounts.log"	

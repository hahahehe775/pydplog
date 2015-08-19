from datetime import date
import os, re

class Log(object):
	"""
	This class represents logs of deppon IT services.

	Li Guanghui 277107

	2015-08-13
	"""
	def __init__(self, service, serverip, instance, logdate, filename="server.log"):
		self.service = service
		self.serverip = serverip
		self.instance = instance
		self.logdate = logdate
		if logdate >= str(date.today()):
			self.filename = filename
		else:
			self.filename = filename + "." + logdate
		self.location = "../jbosslog/"+service+"/"+serverip+"/"+instance+"/"

	def return_log(self,starttime,endtime):
		dateregex = '^[0-9]{4}-(((0[13578]|(10|12))-(0[1-9]|[1-2][0-9]|3[0-1]))|(02-(0[1-9]|[1-2][0-9]))|((0[469]|11)-(0[1-9]|[1-2][0-9]|30)))'
		check = re.compile(dateregex)
		logcontent = []
		# if (starttime == "") and (endtime == ""):
		# 	with open(self.location+self.filename) as fopen:
		# 		for i in fopen:
		# 			logcontent += i
		# 	return logcontent
		# else:
		with open(self.location+self.filename) as fopen:
			for i in fopen:
				# print check.match(i)
				if check.match(i) == None:
					logcontent.append(i.decode('gbk'))
				else:
					if check.match(i):
						logtime = i.split(" ")[1].split(",")[0]
						if logtime >= starttime and logtime <= endtime:
							logcontent.append(i.decode('gbk'))
						elif logtime > endtime:
							break
						else:
		 					pass
		return logcontent

	# def export_log(self,starttime="",endtime=""):
	# 	exportLocation = self.location+"/export/"
	# 	if (starttime is None) and (endtime is None):
	# 		exportLocation = exportLocation + self.filename
	# 		exportFile = open(exportLocation,"w")
	# 		for i in open(self.location+self.filename):
	# 			exportFile.write(i)
	# 		exportFile.close()
	# 	else:
	# 		exportLocation = exportLocation + self.filename +'.'+ starttime +'.'+ endtime
	# 		exportFile = open(exportLocation,"w")
	# 		for i in open(self.location+self.filename):
	# 			logtime = i.split(" ")[1].split(",")[0]
	# 			if logtime > starttime and logtime < endtime:
	# 				exportFile.write(i)
	# 		exportFile.close()

def main():
	print Log('CC','10.249.5.150','call-web01', '2015-08-12','server.log').return_log("07:58","08:10")

	# print cclog.return_log("07:59","09:00")
	# cclog.export_log("07:59:00","09:00:00")

if __name__ == '__main__':
	main()

from datetime import date

class Log(object):
	"""
	This class represents logs of deppon IT services.

	Li Guanghui 277107

	2015-08-13
	"""
	def __init__(self, service, serverip, instance, logdate="", filename="server.log"):
		self.service = service
		self.serverip = serverip
		self.instance = instance
		if logdate >= str(date.today()):
			self.filename = filename
		else:
			self.filename = filename + "." + logdate
		self.location = "../jbosslog/"+service+"/"+serverip+"/"+instance+"/"

	def return_log(self,starttime="",endtime=""):
		logcontent = ''
		if (starttime is None) and (endtime is None):
			for i in open(self.location+self.filename):
				logcontent += i
		else:
			for i in open(self.location+self.filename):
				logtime = i.split(" ")[1].split(",")[0]
				if logtime > starttime and logtime < endtime:
					logcontent += i
		return logcontent

	def export_log(self,starttime="",endtime=""):
		exportLocation = self.location+"/export/"
		if (starttime is None) and (endtime is None):
			exportLocation = exportLocation + self.filename
			exportFile = open(exportLocation,"w")
			for i in open(self.location+self.filename):
				exportFile.write(i)
			exportFile.close()
		else:
			exportLocation = exportLocation + self.filename +'.'+ starttime +'.'+ endtime
			exportFile = open(exportLocation,"w")
			for i in open(self.location+self.filename):
				logtime = i.split(" ")[1].split(",")[0]
				if logtime > starttime and logtime < endtime:
					exportFile.write(i)
			exportFile.close()

def main():
	cclog = Log('CC','10.249.5.150','call-web01', '2015-08-12','server.log')
	print cclog.return_log("07:59:00","09:00:00")
	# cclog.export_log("07:59:00","09:00:00")

if __name__ == '__main__':
	main()

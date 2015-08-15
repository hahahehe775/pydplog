from datetime import date

class Log(object):
	"""
	This class represents logs of deppon IT services.

	Li Guanghui 277107

	2015-08-13
	"""
	def __init__(self, project, serverip, instance, filename="server.log", logdate=""):
		self.project = project
		self.serverip = serverip
		self.instance = instance
		if logdate >= str(date.today()):
			self.filename = filename
		else:
			self.filename = filename + "." + logdate
		self.location = "./"+project+"/"+serverip+"/"+instance+"/"

	def print_log(self,starttime="",endtime=""):
		if (starttime is None) and (endtime is None):
			for i in open(self.location+self.filename):
				print i
		else:
			for i in open(self.location+self.filename):
				logtime = i.split(" ")[1].split(",")[0]
				if logtime > starttime and logtime < endtime:
					print i

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
	cclog = Log('cc','10.249.5.150','call-web01','server.log','2015-08-12')
	# cclog.print_log("07:59:00","09:00:00")
	cclog.export_log("07:59:00","09:00:00")

if __name__ == '__main__':
	main()

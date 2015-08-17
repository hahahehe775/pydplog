from log import Log

cclog = Log('CC','10.249.5.150','call-web01','2015-08-12','server.log')
print cclog.return_log("07:55","08:00")

locationList = getlocation.getlocation('./transwarp/pydplog.db', service_name, warname_name)
locationStr = ''
for i in locationList:
    cclog = Log(service_name, i[0], i[1], today)
    locationStr += cclog.return_log(anhourago, rightnow)
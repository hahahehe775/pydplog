import db

sql_select_instance = 'select server.server_ip, instance.instance_name from service, server, instance, war where service.service_id = instance.service_id and server.server_id=instance.server_id and war.war_id=instance.war_id and service.service_name=\'?\' and war.war_name=\'?\''

result1 = db.select('pydplog.db',sql_select_instance, 'CC', 'call-web.war')
# result = db.select('pydplog.db','select service_name from service')

print result1
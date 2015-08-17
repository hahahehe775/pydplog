def getlocation(file, service_name, war_name):
    
    import db
    
    sql_select_instance = 'select server.server_ip, instance.instance_name from service, server, instance, war where service.service_id = instance.service_id and server.server_id=instance.server_id and war.war_id=instance.war_id and service.service_name=\'?\' and war.war_name=\'?\''
    
    result = db.select(file, sql_select_instance, service_name, war_name)
    # result = db.select('pydplog.db','select service_name from service')
    
    return result
    
if __name__ == '__main__':
    print getlocation('pydplog.db', 'CC', 'call-web.war')
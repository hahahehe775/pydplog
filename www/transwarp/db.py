def connect_cursor(db):
	import sqlite3
	conn = sqlite3.connect(db)
	cursor = conn.cursor()
	return cursor

def connectionClose():
	cursor.close()
	conn.close()

# def connectCtx_select(func):
# 	def wrapper(*args, **kw):
# 		connect_cursor('pydplog.db')
# 		return func(*args, **kw)
# 		connectionClose()
# 	return wrapper 

def select(db, sql, *args):
	cursor = connect_cursor(db)
	sql = sql.replace('?', '%s')
	sql = sql % args
	cursor.execute(sql)
	result = cursor.fetchall()
	# connectionClose()
	return result

def main():
	user = select('pydplog.db','select * from ? where server_id = ?', 'instance', '3')
	print user

if __name__ == '__main__':
	main()
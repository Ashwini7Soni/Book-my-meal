import MySQLdb

db=MySQLdb.connect('localhost','root','1234','ash')

cursor=db.cursor()

print('connection done....')


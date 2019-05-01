from server import sio
from system.mysql import fnSql
from config import *

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)
    sql = 'update user set islogin=0,sid="0" where sid = "%s";'%(sid)
    fnSql(sql)

    

from server import sio
from system.mysql import fnSql
import hashlib
from config import *


@sio.on('updateFriends')
def connect(sid, data):
    print('updateFriends')
    print(data)
    #通过sid查找用户id
    sql0 = 'select * from user where sid = "%s"'%sid;
    res0 = fnSql(sql0)
    #通过用户id，查找好友
    sql1 = 'SELECT *  from user WHERE id in (SELECT user2id from friendrelation WHERE user1id="%s")' % res0[0][0]
    res1 = fnSql(sql1)
    #通过用户id,查找相关性
    sql2 = 'SELECT * from friendrelation WHERE user1id = "%s";' % res0[0][0]
    res2 = fnSql(sql2)
    #通过用户id,查找好友组
    sql3 = 'select * from friend_group where userid = "%s"'% res0[0][0]
    res3 = fnSql(sql3)
    

    data = {
        'res1':list(res1),
        'res2':list(res2),
        'res3':list(res3)
    }
    sio.emit('updateFriends', data, room=sid)

    

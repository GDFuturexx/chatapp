from server import sio
from system.mysql import fnSql
import hashlib
from config import *


@sio.on('sendMessage')
def connect(sid, data):
    print('sendMessage')
    print(data)
    #查找数据库自己的id
    sql0 = 'select * from user where sid = "%s"' % sid
    res0 = fnSql(sql0)
    id = res0[0][0]
    data['sendid'] = id

    


    #查询目标ID是否已经上线
    sql1 = 'select islogin,sid from user where id="%s"'%data['destid'];

    res1 = fnSql(sql1)
    if res1[0][0] == '1':
        sql2 = 'insert into message (sendid,destid,type,content,time,isRead) values ("%s","%s","%s","%s","%s","%s")'%(id,data['destid'],data['type'],data['content'],data['time'],1)
        fnSql(sql2)
        # 查询发送方的信息
        sql3 = 'select * from user where id = "%s"'%id
        print(sql3)
        data['info'] = fnSql(sql3)[0]
        sio.emit('sendMessage',data,room=res1[0][1])
    else:
        #将未读消息插入数据库，下次用户登陆时，接受的消息中未读的消息
        sql2 = 'insert into message (sendid,destid,type,content,time,isRead) values ("%s","%s","%s","%s","%s","%s")'%(id,data['destid'],data['type'],data['content'],data['time'],0)
        fnSql(sql2)
        

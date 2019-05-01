from server import sio
from system.mysql  import fnSql
from config import *
import hashlib


@sio.on('register')
def connect(sid, data):
    # print('register')
    #用户发送注册信息，data={ username:xxx,password:xxxx}
    


    sql = 'select * from user where username="%s";'%data['username']

    sqlres = fnSql(sql)
    if len(sqlres)>0:
        print('注册失败')
        print(sqlres)
        sio.emit('login', 'fail', room=sid)
    else:
        md5password = hashlib.md5(bytes(M_md5num.encode('utf-8'))) #双重加密的加密参数
        md5password.update(bytes(data['password'].encode('utf-8')))

        data['password'] = md5password.hexdigest()
        sql = 'insert into user (username,password,imgheader) values ("%s","%s","%s")'%(data['username'],data['password'],M_userImgheader)
        fnSql(sql)
        print('插入成功')
        sio.emit('register', 'success', room=sid)
        

    #通过数据库查询用户名查看是否已有用户
    #首先要判断是否有这个用户名：
        #如果已存在用户名，告诉用户换一个用户名
    #如果数据库不存次用户名
        #插入用户名、密码加密、默认的信息（性别-》保密，头像--》默认的头像）


from server import sio
from system.mysql import fnSql
import hashlib
from config import *


@sio.on('addFriend')
def connect(sid, data):
    print('addfriend')
    print(data)

    #通过用户名查找是否有这个用户
    sql = 'select * from user where username="%s";' % data['friendname']
    res = fnSql(sql)[0]
    #查找是否已经是好友
    #查找自己的信息

    sql1 = 'select * from user where sid = "%s"'%sid

    selfid = fnSql(sql1)[0][0]

    #查找关系表里面是否自己跟好友已经建立起联系
    sql2 = 'select * from friendrelation where user1id="%s" and user2id="%s"'%(selfid,res[0])
    print(sql2)
    res2 = fnSql(sql2)
    print(res)
    print(res2)

    if len(res)>0 and len(res2)==0:


        #判断好友组表里这个userid有没有这个组
        
        sql4 = 'select * from friend_group where userid="%s" and user_group = "%s"; '%(selfid,data['groupname'])
        #插入数据到好友组里面
        res4 = fnSql(sql4)
        if len(res4) == 0:

            sql3 = 'insert into friend_group (userid,user_group) values (%s,"%s");'%(selfid,data['groupname'])

            #再给朋友和自己建立起联系
            sql5 = 'insert into friend_group (userid,user_group) values (%s,"%s");'%(res[0],data['groupname'])
            print(sql3)
            print(sql5)
            res3 = fnSql(sql3)
            res5 = fnSql(sql5)

            #建立起真正的好友关系
            #先查组ID
            sql6 = 'select * from friend_group where userid = "%s" and user_group = "%s"; '%(selfid,data['groupname'])
            sql7 = 'select * from friend_group where userid = "%s" and user_group = "%s"; '%(res[0],data['groupname'])
            
            
            
            groupid1 =fnSql(sql6)[0][0]


            groupid2 = fnSql(sql7)[0][0]
            #真正给表插入数据


            sql8 = 'insert into friendrelation (user1id,user2id,friend_group_id) values ("%s","%s","%s")'%(selfid,res[0],groupid1)
            sql9 = 'insert into friendrelation (user1id,user2id,friend_group_id) values ("%s","%s","%s")' % (res[0], selfid,groupid2)
            fnSql(sql8)
            fnSql(sql9)

            #查询两个用户的好友数据让其更新
            sio.emit('updateFriends', 'success', room=sid)





    #添加u1,u2 到好友关系表

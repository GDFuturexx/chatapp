import socketio
from server import sio
import eventlet

# from system import *
# from login import * 

from system.connect import *
from system.disconnect import *

from login.login import *
from login.register import *

from chat.addFriend import *
from chat.updateFriends import *



from chat.sendMessage import *







if __name__ == '__main__':
    # sio通过middleware转为应用服务
    app = socketio.Middleware(sio)

    # 依赖eventlet网关服务器
    eventlet.wsgi.server(eventlet.listen(('', 8000)),app)

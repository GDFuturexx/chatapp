from server import sio

@sio.on('connect')
def connect(sid, environ):
    print('connect ', sid)

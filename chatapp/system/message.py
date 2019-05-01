from server import sio

@sio.on('message')
def message(sid, data):
    print('message ', data)

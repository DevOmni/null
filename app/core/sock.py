from app import sio
from flask_socketio import join_room, close_room, leave_room, send, emit


@sio.on('connection')
def connection(data=None):
    if data is not None:
        print(data)
        # data.get('username', False)
    print(data)
    print('Connected')


@sio.on('connected')
def connected(data=None):
    print('Connected to:', data['rcode'])


@sio.on('message')
def message(data):
    print(data['msg'])
    # data = {'msg': 'heres the shited message'}
    sio.emit('message', data)


@sio.on('message', namespace='/yo')  # only works when namespace is "/yo"
def yo_message(data):
    print('exclusive yo:', data)


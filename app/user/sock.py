from app import sio


@sio.on('connect')
def connection(data=None):
    print('Connected')


@sio.on('connected')
def connected(data=None):
    print('Connected to:', data['rcode'])


@sio.on('message')
def message(data):
    print(data['msg'])
    # data = {'msg': 'heres the shited message'}
    sio.emit('message', data)


@sio.on('message', namespace='/yo')
def yo_message(data):
    print('exclusive yo:', data)


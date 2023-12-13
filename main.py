from flask import Flask
from flask_socketio import SocketIO, emit

# Creating a flask app and using it to instantiate a socket object
app = Flask(__name__)
socketio = SocketIO(app)

# values['slider1'] and values['slider2'] store the current value of the sliders
# This is done to prevent data loss on page reload by client.

# Handler for default flask route
# Using jinja template to render html along with slider value as input
@app.route('/')
def index():
    print("Just an information")
    return 'index'

# Handler for a message recieved over 'connect' channel
@socketio.on('connect')
def test_connect():
    print("Just an information")
    emit('after connect',  {'data':'Lets dance'})

# Notice how socketio.run takes care of app instantiation as well.
if __name__ == '__main__':
    socketio.run(app)

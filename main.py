from flask import Flask, request
from flask_socketio import SocketIO,send,emit

app = Flask(__name__)
socketio = SocketIO(app)

url  = None


@socketio.on('connect')
def test_connect():
    print('Client connected')
    socketio.emit("UrlData",{"data":"ashasas"})
    
    
@app.route('/postUrl', methods=['POST'])
def postUrl():
    map = {}
    url1 = request.args.get("url")
    password = request.args.get("password")
    if(str(password) == "OKDONE"):
        global url
        map ={
            "Message" : "URL ADD SUCCESS FULL",
            "Success" : 0,
            "Error Code" : 0
        }
        url = str(url1)
        mapOK ={
            "Url" : url,
            "Success" : 0,
            "Error Code" : 0
        }
        socketio.emit("UrlData",mapOK)
    else:
        map = {
            "Message" : "Url NOT ADD",
            "Success" : -1,
            "Error Code" : -1
        }     
    return map


@app.route('/getUrl', methods=['GET'])
def getUrl():
    map = {}
    if url == None:
        map = {
            "Url " : "Null",
            "Success" : -1,
            "Error Code" : -1
               }
    else:
           map = {
            "Url " : url,
            "Success" : 0,
            "Error Code" : 0
            }
    return map


@app.route('/')
def index():
    return 'index.html'

if __name__ == '__main__':
    socketio.run(app)

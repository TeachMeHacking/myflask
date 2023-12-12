from flask import Flask,request

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome L"

@app.route('/getUrl', methods=['GET'])
def home():
    return "ok Done"


if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')

from flask import Flask,request

app=Flask(__name__)


global url1 

@app.route('/postUrl', methods=['POST'])
def postUrl():
    url = request.args.get("url")
    url = url
    return url


@app.route('/getUrl', methods=['GET'])
def getUrl():
    Url = {}
    if url1 == None:
        Url = {
            "Url" : "Null",
            "Success" : -1,
            "Error Code" : -1
               }
    else:
           Url = {
            "Url" : url1,
            "Success" : 0,
            "Error Code" : 0
            }
    return Url

if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')

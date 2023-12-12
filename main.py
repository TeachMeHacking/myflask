from flask import Flask,request

app=Flask(__name__)


url  = ""



@app.route('/')
def postUrl():
    return "Wlcome On My Site"

@app.route('/postUrl', methods=['POST'])
def postUrl():
    url1 = request.args.get("url")
    global url
    url = str(url1)
    return url


@app.route('/getUrl', methods=['GET'])
def getUrl():
    Url = {}
    if url == None:
        Url = {
            "Url" : "Null",
            "Success" : -1,
            "Error Code" : -1
               }
    else:
           Url = {
            "Url" : url,
            "Success" : 0,
            "Error Code" : 0
            }
    return Url

if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')

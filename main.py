from flask import Flask,request

app=Flask(__name__)


url  = None



@app.route('/')
def wlcome():
    return "Wlcome On My Site"

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
        print(str(url))
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
            "Url " : "Not Available Url",
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

if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')

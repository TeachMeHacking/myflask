from flask import Flask

app=Flask(__name__)

@app.route("/getUrl")
def home():
    return ""


if __name__ == "__main__":
    app.run()#(debug=False,host='0.0.0.0')

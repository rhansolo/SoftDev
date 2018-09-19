from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    print(__name__)
    return 'howdy'
@app.route("/1")
def home2():
    print(__name__)
    return 'HoWdY!'
@app.route("/2")
def home3():
    print(__name__)
    return 'HOWDY!!!'

app.debug = True
app.run()

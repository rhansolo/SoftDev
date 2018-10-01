#Robin Han
#SoftDev pd8
#K13 -- Echo Echo Echo
#2018-09-27

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("button.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request);
    return render_template('newpage.html',user = request.args['username'], method = request.method,greeting = "Suh Suh G Welcome to your page!!")

if __name__ == "__main__":
    app.debug = True
    app.run()

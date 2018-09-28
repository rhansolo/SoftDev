from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    print(app)
    return render_template("button.html")

@app.route("/auth")
def authenticate():
    print(app)
    print(request)
    return "greetings" + request.args["username"] 

if __name__ == "__main__":
    app.debug = True
    app.run()

# Robin Han
# Softdev1 pd8
# K #25: Getting More REST
# 2018-14-11

from flask import Flask, render_template
import urllib.request
import json

app=Flask(__name__)

@app.route("/")
def home():
    #reading api
    url = urllib.request.urlopen("https://restcountries.eu/rest/v2/name/united")
    info = url.read()
    #parsing json object string into a dict
    info = json.loads(info)
    print(info)
    #passing in api values to HTML template
    return render_template("index.html",
                          name = info[0]["name"],
                          population = info[0]["population"],
                          lang = info[0]["nativeName"]
                          )

if __name__=="__main__":
    app.debug=True
    app.run()

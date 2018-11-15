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
    url = urllib.request.urlopen(" https://content.guardianapis.com/search?api-key=1f939f02-73dc-465a-a55a-14aa25c7b5fe")
    info = url.read()

    #parsing json object string into a dict
    info = json.loads(info)

    #passing in api values to HTML template
    return render_template("index.html",
                          section = info["response"]["results"][0]["sectionName"],
                          date = info["response"]["results"][0]["webPublicationDate"],
                          title=info["response"]["results"][0]["webTitle"],
                          link = info["response"]["results"][0]["webUrl"]
                           )

if __name__=="__main__":
    app.debug=True
    app.run()
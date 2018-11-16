# Robin Han
# Softdev1 pd8
# K #26: Getting More REST
# 2018-14-11

from flask import Flask, render_template
import urllib.request
import json

app=Flask(__name__)

@app.route("/")
def home():
    #First API
    #reading api
    url = urllib.request.urlopen("https://restcountries.eu/rest/v2/name/united")
    info = url.read()
    #parsing json object string into a dict
    info = json.loads(info)
    print(info)
    #Second API
    url = urllib.request.urlopen("https://data.cityofnewyork.us/resource/6i93-d96k.json")
    info1 = url.read()
    #parsing json object string into a dict
    info1 = json.loads(info1)
    print(info1)

    url = urllib.request.urlopen("http://numbersapi.com/random/year?json")
    info2 = url.read()
    #parsing json object string into a dict
    info2 = json.loads(info2)
    print(info2)
    #passing in api values to HTML template
    return render_template("index.html",
                          name = info[0]["name"],
                          population = info[0]["population"],
                          lang = info[0]["languages"][0]['nativeName'],
                          street = info1[0]["nta"],
                          boro = info1[0]["bor"],
                          vac_date = info1[0]["vac_date"],
                          vac_area = info1[0]["area_vac"],
                          fact = info2["text"]
                          )

if __name__=="__main__":
    app.debug=True
    app.run()

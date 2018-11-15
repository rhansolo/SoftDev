# Robin Han
# Softdev1 pd8
# K#24: A RESTful Journey Skyward
# 2018-13-11

from flask import Flask, render_template
import json
import urllib.request as request

app = Flask(__name__)

@app.route('/')
def home():
	#reading api
    url = request.urlopen('https://api.nasa.gov/planetary/earth/imagery/?lon=100.75&lat=1.5&date=2014-02-01&cloud_score=True&api_key=JHqhq0229lpFyxDUMspk3tZWC5UIC7Qy6wVjXp9V')
    info = url.read()
    #parsing json object string into a dict
    info = json.loads(info)

    #passing in api values to HTML template
    # image sent to HTML is actually just this image -> https://apod.nasa.gov/apod/image/1811/CaveNebula_Ayoub_960.jpg
    return render_template('index.html', image=info['url'])

if __name__ == '__main__':
    app.debug=True
    app.run()

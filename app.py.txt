from flask import Flask, Response
from utils import generate_rss

app = Flask(__name__)

@app.route('/<username>/rss')
def rss(username):
    xml_data = generate_rss(username)
    return Response(xml_data, mimetype='application/rss+xml')

if __name__ == '__main__':
    app.run()

from flask import Flask

app = Flask(__name__)


@app.route('/')
def home_page():
    return app.send_static_file('infinigen.html')
from flask import Flask, render_template
from data import fav_beer

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', fav_beer=fav_beer)


if __name__ == '__main__':
    app.run()

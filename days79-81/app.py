from flask import Flask, render_template
from data import health_check_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', health_data=health_check_data.get_health_data())


if __name__ == '__main__':
    app.run()

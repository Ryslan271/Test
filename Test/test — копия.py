from flask import Flask
from flask import request
from flask import url_for
from html import Test

app = Flask(__name__)


@app.route('/choice/1')
def choice(Test):
    Test.run()


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

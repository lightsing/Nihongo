from flask import Flask, render_template
from flask_yarn import Yarn

app = Flask(__name__)
yarn = Yarn(app)


@app.route('/')
def hello_world():
    return render_template('index.html',
                           search={
                               'token': '123456',
                               'placeholder': '加油哦'
                           },
                           videos=[{
                               'vid': 1,
                               'name': '标准日本语初级上册 01',
                               'thumb': '/static/img/01.webp',
                               'duration': '01:07:10',
                               'play': 233,
                               'danmu': 0
                           }])


if __name__ == '__main__':
    app.run(debug=True)

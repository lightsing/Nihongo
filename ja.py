from flask import Flask, render_template
from flask_yarn import Yarn

app = Flask(__name__)
yarn = Yarn(app)


@app.route('/')
def index():
    return render_template('index.html',
                           search={
                               'token': '123456',
                               'placeholder': '加油哦'
                           },
                           videos=[{
                               'vid': i,
                               'name': '标准日本语初级上册 {0:02}'.format(i),
                               'thumb': '/static/img/01.webp',
                               'duration': '01:07:10',
                               'play': 233,
                               'danmu': 0
                           } for i in range(1, 11)])


if __name__ == '__main__':
    app.run(debug=True)

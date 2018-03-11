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
                               'vid': 10000 + i,
                               'name': '标准日本语初级上册 {0:02}'.format(i),
                               'thumb': '/static/img/01.webp',
                               'duration': '01:07:10',
                               'play': 233,
                               'danmu': 0
                           } for i in range(1, 11)])


@app.route('/video/av<int:vid>/')
def video(vid):
    return render_template('video.html', search={
                                'token': '123456',
                                'placeholder': '加油哦'
                           }, video={
                                'name': '标准日本语初级上册 {0:02}'.format(vid - 10000),
                                'time': '2018-03-11 14:54',
                                'play': 233,
                                'danmu': 233,
                                'url': '/static/video/01.mp4',
                                'danmu_url': '/static/danmu/01.xml',
                                'up': {
                                    'name': 'Nihongo',
                                    'bio': '君は日本語が本当に上手',
                                    'uploads': 24,
                                    'followers': 1123
                                }
                           })


if __name__ == '__main__':
    app.run(debug=True)

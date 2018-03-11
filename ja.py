from flask import Flask, render_template, abort
from flask_yarn import Yarn
from config import init_app
from models import db, Video, Up

app = Flask(__name__)
init_app(app)
yarn = Yarn(app)
db.app = app
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html',
                           search={
                               'token': '123456',
                               'placeholder': '加油哦'
                           },
                           videos=Video.query.all())


@app.route('/video/av<int:vid>/')
def video(vid):
    try:
        _video = Video.query.filter_by(vid=vid).first()
        _up = Up.query.filter_by(uid=_video.uid).first()
        return render_template('video.html', search={
                                    'token': '123456',
                                    'placeholder': '加油哦'
                               }, video={
                                    'name': _video.name,
                                    'time': _video.time,
                                    'play': _video.play,
                                    'danmu': _video.danmu,
                                    'url': _video.url,
                                    'danmu_url': '/static/danmu/01.xml',
                                    'up': _up
                               })
    except AttributeError:
        return abort(404)


if __name__ == '__main__':

    app.run(debug=True)

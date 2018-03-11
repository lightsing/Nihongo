from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
Column, DateTime, ForeignKey, Integer, String, text = (
    db.Column, db.DateTime, db.ForeignKey, db.Integer, db.String, db.text)
relationship = db.relationship


class Follow(db.Model):
    __tablename__ = 'follow'

    uid = Column(ForeignKey('up.uid', ondelete='CASCADE', onupdate='CASCADE'),
                 primary_key=True, nullable=False, index=True)
    fuid = Column(ForeignKey('up.uid', ondelete='CASCADE', onupdate='CASCADE'),
                  primary_key=True, nullable=False, index=True)
    special = Column(Integer, server_default=text("0"))

    up = relationship('Up', primaryjoin='Follow.fuid == Up.uid')
    up1 = relationship('Up', primaryjoin='Follow.uid == Up.uid')


class Up(db.Model):
    __tablename__ = 'up'

    uid = Column(Integer, primary_key=True)
    name = Column(String(30), nullable=False)
    bio = Column(String(100), server_default=text("'这个人很懒，什么都没有写'"))
    uploads = Column(Integer, server_default=text("0"))
    followers = Column(Integer, server_default=text("0"))
    following = Column(Integer, nullable=False, server_default=text("0"))
    passwd = Column(String(256))
    salt = Column(String(256))


class Video(db.Model):
    __tablename__ = 'video'

    vid = Column(Integer, primary_key=True)
    uid = Column(ForeignKey('up.uid', ondelete='CASCADE', onupdate='CASCADE'), index=True, server_default=text("0"))
    name = Column(String(30), nullable=False)
    time = Column(DateTime, nullable=False, server_default=text("'0000-00-00 00:00:00'"))
    play = Column(Integer, server_default=text("0"))
    danmu = Column(Integer, server_default=text("0"))
    hash = Column(String(64), nullable=False, unique=True)
    format = Column(String(10), server_default=text("'mp4'"))

    up = relationship('Up')

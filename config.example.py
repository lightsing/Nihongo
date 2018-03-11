class dotdict(dict):
    """
    dot.notation access to dictionary attributes
    https://stackoverflow.com/a/23689767/6180554
    """
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


config = dotdict()

config.SQLALCHEMY_TRACK_MODIFICATIONS = False
config.SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
config.qiniu_access_key = 'access_key'
config.qiniu_secret_key = 'secret_key'
config.qiniu_bucket = 'bucket'
config.qiniu_bucket_domain = 'domain'


def init_app(app):
    for k in config:
        app.config[k] = config[k]

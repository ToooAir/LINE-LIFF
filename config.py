config = {
    'LINE_CHANNEL_SECRET': '',
    'LINE_CHANNEL_ACCESS_TOKEN': '',
    'mysql': {
        'dialect': 'mysql',
        'driver': 'pymysql',
        'username': 'line',
        'password': 'linepw',
        'host': 'localhost',
        'database': 'lineDB'
    }
}

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}/{}?charset=utf8".format(
    config['mysql']['dialect'], config['mysql']['driver'], config['mysql']['username'], config['mysql']['password'], config['mysql']['host'], config['mysql']['database'])

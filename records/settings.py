SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}".format(
    'mysql',
    'pymysql',
    'root',
    'kxboons.HK.3JK',
    'gz-cynosdbmysql-grp-av033vrn.sql.tencentcdb.com',
    '24364',
    'als-records'
)
SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://jobly_user:secretpass@localhost:5432/jobly_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

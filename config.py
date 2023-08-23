import os

class Config():
    FLASK_APP = os.environ.get('FLASK_APP') # ????
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_DATABASE_URI = 'postgresql://posvouav:u9mLQVn7CY-3JJNC7MnTDehvpaxY2wsS@batyr.db.elephantsql.com/posvouav'

  
    

    

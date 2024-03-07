from mongoengine import connect
import configparser

def connect_to_db():
    config = configparser.ConfigParser()
    config.read('config.ini')

    mongo_user = config.get('DB', 'user')
    mongodb_pass = config.get('DB', 'pass')
    db_name = config.get('DB', 'db_name')
    domain = config.get('DB', 'domain')

    # Підключення до кластера на AtlasDB за допомогою рядка підключення
    connect(host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority", ssl=True)
    # return connect
# Виклик функції для підключення
# connect_to_db()
from tumbrl import app, database
from tumbrl.models import User, Posts

with app.app_context():
    database.create_all()
    print('Database created!')

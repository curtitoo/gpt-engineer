from config import Config
from models import db
from views import register_blueprints

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

register_blueprints(app)

if __name__ == '__main__':
    app.run()
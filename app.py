from flask import Flask
from socket import gethostname

from config import Config
from models.models import db
from views import views_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(views_bp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    if 'liveconsole' not in gethostname():
        app.run()

from flask import Flask
from .config import Config
from flask_migrate import Migrate
from .models import *
from .routes import *

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(Auth)

db.init_app(app)
migrate = Migrate(app, db)

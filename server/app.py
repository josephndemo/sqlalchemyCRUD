from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from extensions import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

migrate = Migrate(app, db)

CORS(app)

app.secret_key = "sehtrsdyhndtejdydunuyehbdrvteryhe"

# import models AFTER db init
import models

# import views
import views.post


if __name__ == "__main__":
    app.run(debug=True)
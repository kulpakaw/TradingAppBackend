from flask import Flask
from config import Config
from extensions import mongodb, jwt
from auth.user_controller import user_bp

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_bp)

mongodb.init_app(app)
jwt.init_app(app)


if __name__=="__main__":
    app.run(debug=True)
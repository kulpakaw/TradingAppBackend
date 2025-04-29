from flask import Flask
from config import Config
from extensions import mongodb, jwt
from auth.user_controller import user_bp
from tasks.task_controller import tasks_bp
from emails.email_controller import email_bp
from emails.Email_Service import Email_Service

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(user_bp)
app.register_blueprint(tasks_bp)
app.register_blueprint(email_bp)

mongodb.init_app(app)
jwt.init_app(app)
Email_Service.email_init(app)

if __name__=="__main__":
    app.run(debug=True)
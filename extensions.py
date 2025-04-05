from db.mongo import MongoDB
from flask_jwt_extended import JWTManager

mongodb=  MongoDB()
jwt = JWTManager()

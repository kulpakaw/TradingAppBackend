from functools import wraps
from flask import request
import jwt
from utils.json_msg import json_msg
from config import Config

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args,**kwargs):
        
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return json_msg("Brak tokenu","success", 401, error = "Brak tokenu")
        try:
            token = auth_header.split(" ")[1]
            decoded = jwt.decode(token, Config.SECRET_KEY, algorithms = ["HS256"])
            request.user = decoded

        except jwt.ExpiredSignatureError:
            return json_msg("Token wygasł", "error", 401, error = "Token wygasł")
        except jwt.InvalidTokenError:
            return json_msg("Nieprawidłowy token", "error", 401, error = "Nieprawidłowy token")



        return f(*args,**kwargs)

    return decorated_function
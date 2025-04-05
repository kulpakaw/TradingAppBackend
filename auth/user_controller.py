from flask import Blueprint, request
from auth.UserService import UserService
from utils.json_msg import json_msg

user_bp = Blueprint('user', __name__, url_prefix='/api/auth')

@user_bp.route('/register', methods=['POST'])
def register_user():
    try:
        data = request.get_json()
        UserService.create_user(data)
        return json_msg("Utworzono nowe konto", "success", 201)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))


@user_bp.route('/login', methods=['POST'])
def login_user():
    try:
        data = request.get_json()
        UserService.login_user(data)
        return json_msg("Zalogowano pomyślnie", "success", 200)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))
   
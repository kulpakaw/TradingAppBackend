from flask import Blueprint, request
from auth.UserService import UserService
from utils.json_msg import json_msg
from utils.jwt_required import jwt_required

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
        token = UserService.login_user(data)
        return json_msg("Zalogowano pomyślnie", "success", 200, token)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))
    

@user_bp.route("/me", methods=["GET"])
@jwt_required 
def about_me():
    user = request.user 
    return json_msg("Informacje o mnie", "success", 200, user)


@user_bp.route("/change-password", methods=["POST"])
@jwt_required
def change_password():
    try:
        data = request.get_json()
        id  = request.user["user_id"]
        UserService.change_password(data,id)

        return json_msg("Hasło zostało zmienione", "success", 200)
    except Exception as e:
        return json_msg(str(e), "error", 400, str(e))
    

@user_bp.route("/activate/<token>", methods=["GET"])
def activate_user(token):
    user = UserService.get_repo().find_one({"activation_token": token})
    if not user:
        return json_msg("Nieprawidłowy token","error",400)

    UserService.get_repo().update_one(
        {"_id": user["_id"]},
        {"$set": {"is_active": True}, "$unset": {"activation_token": ""}}
    )
    return json_msg("Konto zostało aktywowane!","success",200)

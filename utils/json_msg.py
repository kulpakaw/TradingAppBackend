from flask import jsonify


def json_msg(message,status,code,data=None,error=None):
    return jsonify({
        "message": message,
        "status": status,
        "code": code,
        "data": data,
        "error": error
    }),code
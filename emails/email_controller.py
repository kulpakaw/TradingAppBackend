from flask import Blueprint
from emails.Email_Service import Email_Service

email_bp = Blueprint("emails", __name__, url_prefix="/api/email")

@email_bp.route("/send-email", methods=["POST"])
def create_task():
    result = Email_Service.send_email()
    return result
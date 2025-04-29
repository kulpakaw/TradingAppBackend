from flask import request, jsonify, render_template
from flask_mail import Message, Mail
from werkzeug.utils import secure_filename
import logging

mail = Mail() # Initialize Flask-Mail

class Email_Service:
    
    @staticmethod
    def email_init(app):         
        mail.init_app(app)

    @staticmethod
    def send_activation_email(recipient,token):
        subject = "Aktywuj swoje konto"
        activation_link = f"http://localhost:5000/api/auth/activate/{token}"

        try:
            msg = Message(subject=subject,recipients=[recipient])
            msg.html = render_template('email_activate.html', activation_link=activation_link)

            mail.send(msg)
            logging.info(f"Email sent successfully to {recipient}")

        except Exception as e:
            logging.error(f"Fail to send activation email: {e}")


    @staticmethod
    def send_email():
        data = request.get_json()
        subject = data["subject"]
        recipient = data["recipient"]
        body = data["body"]
        #attachment_path = data["attachment_path"]

        try:
            msg = Message(subject=[subject], recipients=[recipient])
            #msg.body = body
            # Render HTML template and pass dynamic data
            msg.html = render_template('email_welcome.html',name="Adrian Sz")

            # # Attach the generated report file
            # with open(attachment_path, 'rb') as f:
            #     msg.attach(secure_filename(attachment_path), 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', f.read())
            
            mail.send(msg)
            logging.info(f"✅ Email sent successfully to {recipient} with the attachment.")

            return jsonify({
                "message": "Wysłano wiadomość",
                "data": body,
                # "attachment_path": attachment_path
            }),200

        except Exception as e:
            logging.error(f"❌ Failed to send email: {e}")
            return jsonify({
                "message": "Nie udało się wysłać wiadomości",
            })
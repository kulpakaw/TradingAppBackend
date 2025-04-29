from marshmallow import Schema, fields, validate, ValidationError, EXCLUDE
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
import re
from datetime import datetime

def is_password_strong(password):
    if len(password) < 8:
        return False, "Hasło musi zawierać co najmniej 8 znaków."
    if not re.search(r"[A-Z]", password):
        return False, "Hasło musi zawierać przynajmniej jedną dużą literę."
    if not re.search(r"[0-9]", password): 
        return False, "Hasło musi zawierać przynajmniej jedną cyfrę."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): 
        return False, "Hasło musi zawierać przynajmniej jeden znak specjalny."
    return True, ""

class UserModel(Schema): 
    id = fields.Str(dump_only=True)
    username = fields.Str(required=True, validate=validate.Length(min=3, max=50))
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    account_type = fields.Str(required=True, validate=validate.OneOf(["admin", "user"]))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    is_active = fields.Bool(dump_only=True)
    activation_token = fields.Str(dump_only=True)

    class Meta:
        unknown = EXCLUDE

    def load(self, data, **kwargs):
        UserModel.validate_password(data["password"])
        data["password"] = UserModel.hash_password(data["password"])
        data["is_active"] = False
        data["activation_token"] = str(uuid.uuid4())
        data["created_at"] = datetime.utcnow()
        data["updated_at"] = datetime.utcnow()
        return super().load(data, **kwargs)

    def validate_password(password): 
        is_strong, message = is_password_strong(password)
        if not is_strong:
            raise ValidationError(message)

    def hash_password(password):
        return generate_password_hash(password)

    def check_password(old, password):
        return check_password_hash(old, password)
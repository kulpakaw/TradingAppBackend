from marshmallow import Schema,fields

class TaskModel(Schema): 
    name = fields.Str(required=True,dump_only=True)
    description = fields.Str(required=True)
    priority = fields.Email(required=True)
    term = fields.Str(required=True, load_only=True)
    

def load(self, data, **kwargs):
        return super().load(data, **kwargs)

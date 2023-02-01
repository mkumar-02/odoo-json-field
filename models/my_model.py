import json
from odoo import models,fields,api


class JSONField(fields.Field):

    type = 'json'
    column_type = ('json', 'json')

    def __init__(self, string, **kwargs):
        self.column_type = ('json', 'json')

        super(JSONField, self).__init__(string= string, **kwargs)

    def convert_to_cache(self, value, record, validate=True):
        if value and not isinstance(value, dict):
            return json.loads(value)
        return value

    def convert_to_record(self, value, record):
        if value:
            return json.dumps(value)
        return value


class MyModel(models.Model):
    _name = "my.model"
    _description = "creating the custom model"

    name = fields.Char(string="Name")
    additional_data = JSONField("Additonal Data")



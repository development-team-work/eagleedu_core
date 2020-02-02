from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime

class EagleeduRegisterbook(models.Model):
    _name='eagleedu.registerbook'
    _description='this admission register book'
    name=fields.Char('Register Book Name' ,compute='get_name')
    standard=fields.Many2one('eagleedu.standard_class',required=True)
    academic_year=fields.Many2one('eagleedu.academic_year', "For the year" , required=True)
    start_time = fields.Datetime(string='Application Starts on',default=lambda self: fields.datetime.now())
    end_time = fields.Datetime(string='Application ends on',default=lambda self: fields.datetime.now())
    active=fields.Boolean('Is active', default='True')
    @api.onchange('standard_class','academic_year')
    def get_name(self):
        for rec in self:
            if rec.standard_class and rec.academic_year:
                rec.name=rec.standard_class.name +'-'+rec.academic_year.name+' '+'Admission'
# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSyllabus(models.Model):
    _name = 'eagleedu.syllabus'
    _description = "Syllabus "
    _rec_name='syllabus_display'

    syllabus_name = fields.Char(string='Syllabus Name', help="Enter the Name of the Syllabus")
    syllabus_code = fields.Char(string='Syllabus Code', help="Enter the Code of the Syllabus")
    syllabus_display=fields.Char('Syllabus Display',help="This is printed on the marksheet as Subject")


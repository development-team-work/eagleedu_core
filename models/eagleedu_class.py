# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduClass(models.Model):
    _name = 'eagleedu.class'
    _description = "Class Standard Level"
    sequence=fields.Integer("Sequence")
    class_name = fields.Char(string='Class Name', required=True, help="Enter the Name of the Class")
    roman_name = fields.Char(string='Roman Name ', help="Enter the Code of the Class")
    # section_ids=fields.Many2many('education.class.section',column2='level_ids',column1='section_ids',string='Sections')
    # syllabus_ids = fields.One2many('education.syllabus', 'class_id')
    # division_ids = fields.Many2many('education.division''class_id', 'class_id')
    # division_ids=fields.Many2many('education.division','class_dev_rel','division_ids','classes_ids')

# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSubject(models.Model):
    _name = 'eagleedu.subject'
    _description = "Subject "
    subject_name = fields.Char(string='Subject Name', help="Enter the Name of the Subject")
    subject_code = fields.Char(string='Subject Code', help="Enter the Code of the Subject")
    # section_ids=fields.Many2many('education.class.section',column2='level_ids',column1='section_ids',string='Sections')
    # syllabus_ids = fields.One2many('education.syllabus', 'class_id')
    # division_ids = fields.Many2many('education.division''class_id', 'class_id')
    # division_ids=fields.Many2many('education.division','class_dev_rel','division_ids','classes_ids')

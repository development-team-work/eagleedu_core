# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduClassDivision(models.Model):
    _name = 'eagleedu.class.division'
    _description = "Class room"

    name = fields.Char(string='Class Division Name')
    instructor_id = fields.Many2one('eagleedu.instructor', string='Instructor Name', help="Class teacher/Faculty")
    instructor_name = fields.Many2one('eagleedu.instructor', 'name', help="Class teacher/Faculty")
    academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year',
                                        help="Select the Academic Year", required=True)
    standard_class = fields.Many2one('eagleedu.standard_class', string='Standard Class', required=True,
                                help="Select the Class")
    class_section_id = fields.Many2one('eagleedu.class_section', string='Section', help="Select the Section")
    #

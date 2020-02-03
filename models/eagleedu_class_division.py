# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduClassDivision(models.Model):
    _name = 'eagleedu.class.division'
    _description = "Class room"

    name = fields.Char(string='Name')
    display=fields.Char('Class Name')
    actual_strength = fields.Integer(string='Max student No', help="Total strength of the class")
    faculty_id = fields.Many2one('eagleedu.faculty', string='Class Teacher', help="Class teacher/Faculty")
    # class_division_id = fields.Char('eagleedu.class.division', string='Class Division', help="Class Division")
    academic_year_id = fields.Many2one('eagleedu.academic.year', string='Academic Year',
                                       help="Select the Academic Year", required=True)
    standard_class = fields.Many2one('eagleedu.standard_class', string='Class', required=True,
                               help="Select the Class")
    division_id = fields.Many2one('eagleedu.group_division', string='Group Division',help="Select the Division")
    section_id = fields.Many2one('eagleedu.class_section', string='Section', help="Select the Section")
    students_ids = fields.One2many('eagleedu.student', 'standard_class', string='Students')
    student_count = fields.Integer(string='Students Count', compute='_get_student_count')
    # class_room=fields.Many2one('education.rooms','Room No')

# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduClass(models.Model):
    _name = 'eagleedu.class'
    _description = "Class Standard Level"
    sequence=fields.Integer("Sequence")
    name = fields.Char(string='Class', required=True, help="Enter the Name of the Class")
    class_id = fields.Many2one('eagleedu.class', string='Class', help="Enter the Name of the Class")
#    class_ids = fields.Many2many('eagleedu.class', string='Classes', help="Enter the Name of the Class")
    section_id = fields.Many2one('eagleedu.section', string='Section Name', help="Enter the Name of the Section")
    sections_ids = fields.Many2many('eagleedu.section', string='Sections Names', help="Enter the Name of the Section")
    roman_name = fields.Char(string='Roman Name ', help="Enter the Code of the Class")

    groupdivision_id = fields.Many2one('eagleedu.groupdivision', string='Group Division', help="Enter the Name of the Group division")
    groupdivision_ids = fields.Many2many('eagleedu.groupdivision', string='Groups Divisions', help="Enter the Name of the Group division")

    # section_ids=fields.Many2many('education.class.section',column2='level_ids',column1='section_ids',string='Sections')
    # syllabus_ids = fields.One2many('education.syllabus', 'class_id') #
    # division_ids = fields.Many2many('education.division''class_id', 'class_id')
    # division_ids=fields.Many2many('education.division','class_dev_rel','division_ids','classes_ids')

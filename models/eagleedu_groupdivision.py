# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSection(models.Model):
    _name = 'eagleedu.groupdivision'
    _description = "Group Division "
    name = fields.Char(string='Group Division', help="Enter the Name of the Group Division")

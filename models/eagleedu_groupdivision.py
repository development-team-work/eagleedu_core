# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduGroupdivision(models.Model):
    _name = 'eagleedu.groupdivision'
    _description = "Group Division "
    name = fields.Char(string='Group Division', help="Enter the Name of the Group Division")
    groupdivisions_ids = fields.Many2many('eagleedu.groupdivision', 'eagleedu_groupdivision_rel', 'groupdivisions_ids')



    # compulsory_for = fields.Many2many('education.class.history', 'education_syllabus_class_history_rel',
    #                                   'compulsory_for', 'compulsory_subjects', 'compulsory for')


    def view_groupdivisions(self):
        """Return the list of current students in this class"""
        self.ensure_one()
        groupdivisions = self.env['eagleedu.groupdivision'].search([('class_id', '=', self.id)])
        groupdivisions_list = groupdivisions.mapped('id')
        return {
            'domain': [('id', 'in', groupdivisions_list)],
            'name': _('Group Division'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'eagleedu.groupdivision',
            'view_id': False,
            # 'context': {'default_classes_ids': self.id},
            'type': 'ir.actions.act_window'
        }
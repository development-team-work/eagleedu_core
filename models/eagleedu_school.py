from eagle import fields, models

class EducationInstitute(models.Model):
   _inherit = 'res.company'
    
   affiliation = fields.Char(string='Affiliation')
   Registration_no = fields.Char(string='Registration No')
   ein_no = fields.Char(string='EIN No')
   base_class = fields.Many2one('education.class', string="Lower class")
   higher_class = fields.Many2one('education.class', string="Higher class")
   #todo here to implement Head campus like 
   # parent_id=fields.Many2one("res.company","parent Campus")
   # avoide parent child recurrency here

class Education_Shift(models.Model):
  _name ='eagleedu.shift'
  _description="this model represents shift of a school ie.Morning,Day,Evening etc"
  name=fields.Char("Shift")
  description=Fields.Char("description")
  

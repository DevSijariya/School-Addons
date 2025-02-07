from odoo import models ,fields

from .model import CommonDetails


class TeacherDetail(models.Model):
    """
    Description: Student Class which is used to store Teacher information
    """
    _name = "teacher.information" # Set the name of the new model
    _description = "This model is used to store the information of the teacher"
    _inherit = 'common.details' # Inherit the Abstract model
    subject = fields.Char("Subject")
    salary=fields.Integer("Salary")

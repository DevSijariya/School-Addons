#Importing the odoo Basic Modules
from odoo import models, fields



class CommonDetails(models.AbstractModel):
    """
    Description : Creating the Abstract model which contain the common feilds for both the students and the teacher
    
    """
    _name = "common.details" # Set the name of the new model
    _description = "Contain Common Informations"
    name = fields.Char("Name")
    age = fields.Integer("Age")
    date_of_birth = fields.Date("Date of Birth")
    profile_pic = fields.Image("Image")


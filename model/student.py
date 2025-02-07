from odoo import models ,fields
import logging
_logger = logging.getLogger(__name__)

class StudentDetail(models.Model):
    """
    Description: Student Class which is used to store student information
    """
    _name = "student.information" # Set the name of the new model
    _description = "This Model is used to store the information of the student "
    _inherit="common.details"
    roll_number = fields.Integer("Roll Number")
    branch = fields.Char("Branch")
    admission_date=fields.Date('Admission Date')
    leaving_date=fields.Date('leaving Date')
    section = fields.Selection([('A', 'A'), ('B', 'B'),('C','C'),('D','D')])
    teacher_id=fields.Many2one(comodel_name='teacher.information',string="class Teacher")
    
    def create(self, vals):
        """
        Description: Create a new student record.
        """

        if 'roll_number' in vals:
            # Example logic: Ensure roll number is unique
            existing_student = self.env['student.information'].search([('roll_number', '=', vals['roll_number'])])
            if existing_student:
                _logger.exception("----------IT IS exception---------")
                raise ValueError("Roll Number already exists.")
        # Call the parent class's create method to actually create the record
            else:
                _logger.info("\n Data Created \n")
        return super(StudentDetail, self).create(vals)

    def write(self, vals):
        """
        Description: Update student records.
        """
        _logger.info("\n---------Age Set To Default--------\n")
        if 'age' in vals:
            vals['age'] = 21  # Custom logic to update the age field if present

        # Call the parent class's write method
        return super(StudentDetail, self).write(vals)


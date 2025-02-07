from odoo.tests import TransactionCase
import logging

_logger = logging.getLogger(__name__)


_logger.warning('Before Class')

class TestModule(TransactionCase):
        """
        Description : Creating the testing class which can test the student model functionality
        """
        _logger.warning('Inside Class')

        def setUp(self):
            _logger.warning('Method Executed in setUp')

        
            super(TestModule,self).setUp()
        def test_create_student(self):
            student = self.env['student.information'].create({
            'name': 'John Doe',
            'age': 22,
            'branch': 'CSE',
            'roll_number': 10,
            'date_of_birth': '2001-01-01',
            'admission_date': '2021-09-01',
            'leaving_date': '2025-06-01',
            'section': 'A',
            })

            self.assertEqual(student.name, 'John Doe',msg="test Case 1 pass")
            self.assertEqual(student.age, 22)
            self.assertNotEqual(student.branch, 'CSE')
            self.assertEqual(student.roll_number, 10)
            
        def test_unique_roll_number(self):
            # Create a student with a specific roll number
            self.env['student.information'].create({
                'name': 'Jane Smith',
                'age': 21,
                'branch': 'ECE',
                'roll_number': 20,
                'date_of_birth': '2002-05-10',
                'admission_date': '2022-05-01',
                'leaving_date': '2026-05-01',
                'section': 'B',
            })
            
            # Try to create another student with the same roll number (this should raise an error)
            with self.assertRaises(ValueError):
                self.env['student.information'].create({
                    'name': 'John Adams',
                    'age': 23,
                    'branch': 'IT',
                    'roll_number': 20,  # Same roll number as above
                    'date_of_birth': '2000-11-12',
                    'admission_date': '2021-10-01',
                    'leaving_date': '2025-10-01',
                    'section': 'C',
            })
from django.test import TestCase
from .forms import RegistrationForm, LoginForm, SectionOneForm, SectionTwoForm

class RegistrationFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'username': 'ChrisCornell',
            'email': 'chriscornell@example.com',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        form = RegistrationForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_password_mismatch(self):
        form_data = {
            'username': 'ChrisCornell',
            'email': 'chriscornell@example.com',
            'password': 'password123',
            'confirm_password': 'password456'  
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        form_data = {
            'username': 'ChrisCornell',
            'email': 'invalid-email',
            'password': 'password123',
            'confirm_password': 'password123'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())


class LoginFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'username': 'chriscornell@example.com',
            'password': 'password123'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_email(self):
        form_data = {
            'username': '',  # Empty email
            'password': 'password123'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())


class SectionOneFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'applicant_name': 'Chris Cornell',
            'residential_address': '123 Main St, Sydney',
            'date_of_birth': '1990-01-01',
            'customer_number': 12345,
            'held_license': 'Yes',
            'current_license': 'Yes',
            'license_number': 'NSW123456',
            'license_class': 'C',
            'expiry_date': '2025-12-31',
            'medical_review': 'No',
            'agree_submission': True,
            'declaration_date': '2024-10-11'
        }
        form = SectionOneForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_name(self):
        form_data = {
            'applicant_name': '',  # Missing name
            'residential_address': '123 Main St, Sydney',
            'date_of_birth': '1990-01-01',
            'customer_number': 12345,
            'held_license': 'Yes',
            'current_license': 'Yes',
            'license_number': 'NSW123456',
            'license_class': 'C',
            'expiry_date': '2025-12-31',
            'medical_review': 'No',
            'agree_submission': True,
            'declaration_date': '2024-10-11'
        }
        form = SectionOneForm(data=form_data)
        self.assertFalse(form.is_valid())


class SectionTwoFormTest(TestCase):

    def test_valid_form(self):
        form_data = {
            'disability': 'paraplegia',
            'condition_temp': 'isTemporary',
            'period': 6,
            'agree_declaration': True,
            'agree_submission': True
        }
        form = SectionTwoForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_missing_disability(self):
        form_data = {
            'disability': '',  
            'condition_temp': 'isTemporary',
            'period': 6,
            'agree_declaration': True,
            'agree_submission': True
        }
        form = SectionTwoForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_invalid_period(self):
        form_data = {
            'disability': 'paraplegia',
            'condition_temp': 'isTemporary',
            'period': -1,  
            'agree_declaration': True,
            'agree_submission': True
        }
        form = SectionTwoForm(data=form_data)
        self.assertFalse(form.is_valid())











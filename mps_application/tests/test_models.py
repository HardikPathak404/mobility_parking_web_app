from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from ..models import Resident, MedicalPractitioner, Application
# Create your tests here.


class ResidentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')
        self.resident = Resident.objects.create(
            user=self.user,
            date_of_birth='1990-01-01',
            phone_number='1234567890',
            address='123 Test St',
            postal_code='1234'
        )

    def test_resident_creation(self):
        try:
            self.assertEqual(self.resident.user.username, 'resident_user')
            self.assertEqual(self.resident.phone_number, '1234567890')
            print("Test 1 [User Resident Creation (All Valid Fields)] - Passed ")
        except AssertionError:
            print("Test 1 (User Resident Creation) - Failed")
            raise



class ResidentPhoneNumberTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_phone_number(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990-01-01',
            phone_number='123456789123456789',  # The phone number has more values than the maximum required
            address='123 Test St',
            postal_code='1234'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 1.1 [Invalid Phone Number (Resident)] Test - passed")

class ResidentDateOfBirthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_date_of_birth(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990', #Date field is invalid
            phone_number='1234567890',  
            address='123 Parramatta St',
            postal_code='1234'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 1.2 [Invalid Date of Birth (Resident)] Test - passed")

class ResidentAddressTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_address(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990',
            phone_number='1234567890',  
            address=None, #Address field is set to none which is not valid
            postal_code='1234'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 1.3 [Invalid Address (Resident)] Test - passed")

class ResidentPostalCodeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_date_of_birth(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990-09-09',
            phone_number='1234567890',  
            address='123 Parramatta St',
            postal_code='1234567' #Postal code has more values than maximum required
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 1.4 [Invalid Postal Code (Resident)] Test - passed")




class MedicalPractitionerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='doctor_user', password='password')
        self.medical_practitioner = MedicalPractitioner.objects.create(
            user=self.user,
            date_of_birth='1985-05-05',
            phone_number='0987654321',
            address='456 Medical Ave',
            postal_code='5678'
        )

    def test_medical_practitioner_creation(self):
        try:
            self.assertEqual(self.medical_practitioner.user.username, 'doctor_user')
            self.assertEqual(self.medical_practitioner.address, '456 Medical Ave')
            print("Test 2 [User Medical Practioner Creation (All Valid Fields)] - Passed")
        except AssertionError:
            print("Test 2 (User Medical Practitioner Creation) - Failed")
            raise

class MedicalPractitionerDateOfBirthTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_date_of_birth(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990-09-0999', #Invalid date format
            phone_number='1234567890',  
            address='123 Parramatta St',
            postal_code='1234'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 2.1 [Invalid Date Of Birth Test (Medical Practitioner)] - passed")


class MedicalPractitionerPhoneNumberTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_phone_number(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990-09-09',
            phone_number='123456789012345678',  # Phone number has more values than maximum required
            address='123 Parramatta St',
            postal_code='1234'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 2.2 [Invalid Phone Number Test (Medical Practitioner)] - passed")


class MedicalPractitionerAddressTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_address(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990-09-09',
            phone_number='1234567890',  
            address=None, #Address field set to none
            postal_code='1234'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 2.3 [Invalid Address Test (Medical Practitioner)] - passed")



class MedicalPractitionerPostalCodeTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')

    def test_invalid_postal_code(self):
        resident = Resident(
            user=self.user,
            date_of_birth='1990-09-09',
            phone_number='1234567890',  
            address='123 SEF Tutorial',
            postal_code='12345678'
        )
        
        # Ensure a ValidationError is raised when calling full_clean
        with self.assertRaises(ValidationError):
            resident.full_clean()
            raise
        print("Test 2.4 [Invalid Postal Code (Medical Practitioner)] - passed")


class ApplicationModelTest(TestCase):
    def setUp(self):
        self.resident_user = User.objects.create_user(username='resident_user', password='password')
        self.medical_user = User.objects.create_user(username='doctor_user', password='password')
        self.resident = Resident.objects.create(user=self.resident_user, date_of_birth='1990-01-01', phone_number='1234567890', address='123 Test St', postal_code='1234')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.medical_user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        self.application = Application.objects.create(
            resident=self.resident,
            medical_practitioner=self.medical_practitioner,
            status='RR',
            permit_type='INDI',
            application_type='NEW',
            held_license='Yes',
            current_license='Yes',
            medical_review='No',
            medical_condition='No',
            disability='None',
            epilepsy='No'
        )

    def test_application_creation(self):
        try:
            self.assertEqual(self.application.resident.user.username, 'resident_user')
            self.assertEqual(self.application.medical_practitioner.user.username, 'doctor_user')
            self.assertEqual(self.application.status, 'RR')
            print("Test 3 [Application Creation (All Valid Fields)] - Passed")
        except AssertionError:
            print("Test 3 (Application Creation) - Failed")



#Relationship between Medical Practitioner and Application
class ResidentApplicationRelationshipTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')
        self.resident = Resident.objects.create(user=self.user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')

    def test_resident_application_relationship(self):
        application = Application.objects.create(
            resident=self.resident,  
            medical_practitioner=self.medical_practitioner, 
            status='RR',
            permit_type='INDI',
            application_type='NEW'
        )
        self.assertEqual(application.resident, self.resident)
        print("Test 3.1 (Resident and Application Relationship) - Passed")

#Relationship between Medical Practitioner and Application
class MedicalPractitionerApplicationRelationshipTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='resident_user', password='password')
        self.resident = Resident.objects.create(user=self.user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')

    def test_resident_application_relationship(self):
        application = Application.objects.create(
            resident=self.resident,  
            medical_practitioner=self.medical_practitioner, 
            status='RR',
            permit_type='INDI',
            application_type='NEW'
        )
        self.assertEqual(application.medical_practitioner, self.medical_practitioner)
        print("Test 3.2 (Medical Practitioner and Application Relationship) - Passed")

class ApplicationStatusTest(TestCase):
    def setUp(self):
        self.resident_user = User.objects.create_user(username='resident_user', password='password')
        self.medical_user = User.objects.create_user(username='doctor_user', password='password')
        self.resident = Resident.objects.create(user=self.resident_user, date_of_birth='1990-01-01', phone_number='1234567890', address='123 Test St', postal_code='1234')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.medical_user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        

    def test_application_status(self):
        application = Application(
            resident=self.resident,
            medical_practitioner=self.medical_practitioner,
            status='RRRRR', #Invalid status field. Value not part of choices
            permit_type='INDI',
            application_type='NEW',
            held_license='Yes',
            current_license='Yes',
            medical_review='No',
            medical_condition='No',
            disability='None',
            epilepsy='No'
        )

        with self.assertRaises(ValidationError):
            application.full_clean()
            raise
        print("Application Status Test - passed")


class PermitTypeTest(TestCase):
    def setUp(self):
        self.resident_user = User.objects.create_user(username='resident_user', password='password')
        self.medical_user = User.objects.create_user(username='doctor_user', password='password')
        self.resident = Resident.objects.create(user=self.resident_user, date_of_birth='1990-01-01', phone_number='1234567890', address='123 Test St', postal_code='1234')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.medical_user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        

    def test_permit_type(self):
        application = Application(
            resident=self.resident,
            medical_practitioner=self.medical_practitioner,
            status='RR', 
            permit_type='INDIVIDUAL', #Invalid permit type field. Value not part of choices
            application_type='NEW',
            held_license='Yes',
            current_license='Yes',
            medical_review='No',
            medical_condition='No',
            disability='None',
            epilepsy='No'
        )

        with self.assertRaises(ValidationError):
            application.full_clean()
            raise
        print("Application permit type Test - passed")

class ApplicationTypeTest(TestCase):
    def setUp(self):
        self.resident_user = User.objects.create_user(username='resident_user', password='password')
        self.medical_user = User.objects.create_user(username='doctor_user', password='password')
        self.resident = Resident.objects.create(user=self.resident_user, date_of_birth='1990-01-01', phone_number='1234567890', address='123 Test St', postal_code='1234')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.medical_user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        

    def test_application_type(self):
        application = Application(
            resident=self.resident,
            medical_practitioner=self.medical_practitioner,
            status='RR', 
            permit_type='INDI', 
            application_type=None, #Invalid application type field. Application type cannot be none
            held_license='Yes',
            current_license='Yes',
            medical_review='No',
            medical_condition='No',
            disability='None',
            epilepsy='No'
        )

        with self.assertRaises(ValidationError):
            application.full_clean()
            raise
        print("Application type Test - passed")


class HeldLicenseTest(TestCase):
    def setUp(self):
        self.resident_user = User.objects.create_user(username='resident_user', password='password')
        self.medical_user = User.objects.create_user(username='doctor_user', password='password')
        self.resident = Resident.objects.create(user=self.resident_user, date_of_birth='1990-01-01', phone_number='1234567890', address='123 Test St', postal_code='1234')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.medical_user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        

    def test_held_license(self):
        application = Application(
            resident=self.resident,
            medical_practitioner=self.medical_practitioner,
            status='RR', 
            permit_type='INDI', 
            application_type='NEW', 
            held_license='YES', #Testing YES instead of yes
            current_license='Yes',
            medical_review='No',
            medical_condition='No',
            disability='None',
            epilepsy='No'
        )

        with self.assertRaises(ValidationError):
            application.full_clean()
            raise
        print("Held License Test - passed")

class CurrentLicenseTest(TestCase):
    def setUp(self):
        self.resident_user = User.objects.create_user(username='resident_user', password='password')
        self.medical_user = User.objects.create_user(username='doctor_user', password='password')
        self.resident = Resident.objects.create(user=self.resident_user, date_of_birth='1990-01-01', phone_number='1234567890', address='123 Test St', postal_code='1234')
        self.medical_practitioner = MedicalPractitioner.objects.create(user=self.medical_user, date_of_birth='1985-05-05', phone_number='0987654321', address='456 Medical Ave', postal_code='5678')
        

    def test_current_license(self):
        application = Application(
            resident=self.resident,
            medical_practitioner=self.medical_practitioner,
            status='RR', 
            permit_type='INDI', 
            application_type='NEW', 
            held_license='Yes', 
            current_license='YES', #Testing YES instead of yes
            medical_review='No',
            medical_condition='No',
            disability='None',
            epilepsy='No'
        )

        with self.assertRaises(ValidationError):
            application.full_clean()
            raise
        print("Current License Test - passed")



from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from mps_application.models import Resident, Application, MedicalPractitioner

class MPSViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.resident = Resident.objects.create(user=self.user,
            date_of_birth='1990-01-01',
            phone_number='1234567890',
            address='123 Test St',
            postal_code='1234')
        
        self.medical_practitioner = MedicalPractitioner.objects.create(
            user=self.user,
            date_of_birth='1980-01-01',
            phone_number='0987654321',
            address='456 Practitioner Rd',
            postal_code='5678'
        )
    
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
        )

    

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/homepage.html')

    def test_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_view_post_success(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('home'))

    def test_login_view_post_failure(self):
        response = self.client.post(reverse('login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertContains(response, 'Please enter a correct username and password.')

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))

    def test_profile_view_redirects_if_not_logged_in(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('login') + '?next=/profile/')

    def test_profile_view_logged_in(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/profile.html')

    def test_section_one_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('sectionOne'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionOne.html')

    def test_section_one_view_post_success(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('sectionOne'), {
            'permitType': 'TEMP',
            'applicationType': 'NEW',
            'heldLicense': 'Yes',
            'currentLicense': 'Yes',
            'licenseNumber': '1234567890',
            'licenseClass': 'C',
            'expiry': '2025-01-01',
            'medicalReview': 'No',
            'othername': 'othername'
        })
        self.assertEqual(response.status_code, 302) 
        self.assertRedirects(response, reverse('profile'))

    def test_section_one_view_post_failure(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('sectionOne'), {
            'permitType': '',
            'applicationType': '',
            'heldLicense': '',
            'currentLicense': '',
            'medicalReview': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionOne.html')
        self.assertContains(response, 'Permit type is required.')

    def test_section_two_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('sectionTwo', args=[self.application.application_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionTwo.html')

    def test_section_two_view_post_success(self):
        self.client.login(username='testuser', password='testpassword')
        application = Application.objects.create(
            resident=self.resident,
            status='RR',
            permit_type='TEMP', 
            application_type='NEW',
        )
        response = self.client.post(reverse('sectionTwo', args=[application.application_id]), {
            'disability': 'Mobility',
            'conditionTemp': 'Yes',    
            'period': '3',                
            'action': 'Submit'              
        })
        if response.status_code != 302:
            print(response.content)
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('profile'))

    def test_section_two_view_post_failure(self):
        self.client.login(username='testuser', password='testpassword')
        application = Application.objects.create(
            resident=self.resident, 
            status='RR', 
            permit_type='TEMP', 
        )
        response = self.client.post(reverse('sectionTwo', args=[application.application_id]), {
            'disability': '',              
            'conditionTemp': '',           
            'period': '',                  
            'action': 'Submit'             
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionTwo.html')
 

    def test_section_three_view_get(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('sectionThree', args=[self.application.application_id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionThree.html')

    def test_section_three_view_post_success(self):
        self.client.login(username='testuser', password='testpassword')
        application = Application.objects.create(
            resident=self.resident, 
            medical_practitioner=self.medical_practitioner, 
            status='RR'
        )
        response = self.client.post(reverse('sectionThree', args=[application.application_id]), {
            'years': '5',                             
            'months': '3',                            
            'Epilepsy': 'Yes',                       
            'epilepsy-onset': '2021-01-01',         
            'epilepsy-last-seizure': '2021-02-01',  
            'Certification': 'Fit',                    
            'action': 'Submit'          
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('profile'))

    def test_section_three_view_post_failure(self):
        self.client.login(username='testuser', password='testpassword')
        application = Application.objects.create(resident=self.resident, status='RR')
        response = self.client.post(reverse('sectionThree', args=[application.application_id]), {
            'doctorName': '',
            'providerNumber': '',
            'doctorPhone': '',
            'epilepsy': ''
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionThree.html')
        self.assertContains(response, 'Epilepsy status is required.')

    def test_section_three_view_post_failure(self):
        self.client.login(username='testuser', password='testpassword')
        application = Application.objects.create(resident=self.resident, status='RR')
        response = self.client.post(reverse('sectionThree', args=[application.application_id]), {
            'doctorName': '',
            'providerNumber': '',
            'doctorPhone': '',
            'epilepsy': '',
            'action': 'Submit'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/sectionThree.html')
        self.assertContains(response, 'Doctor certificate is required.')

    def test_show_applications_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('applications'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'mps_application/applications.html')

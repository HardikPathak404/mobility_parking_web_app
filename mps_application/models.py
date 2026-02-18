from django.db import models
from django.contrib.auth.models import User


class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200, default="")
    postal_code = models.CharField(max_length=4, default="")
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 

class MedicalPractitioner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200, default="")
    postal_code = models.CharField(max_length=4, default="")
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}" 

class Application(models.Model):
    application_id = models.AutoField(primary_key=True)
    resident = models.ForeignKey(Resident, on_delete=models.CASCADE)
    medical_practitioner = models.ForeignKey(MedicalPractitioner, on_delete=models.CASCADE, null=True, blank=True)
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=[('RR', 'Review Ready'), ('DR', 'Draft'), ('RE', 'Reviewed')], default='RR')
    permit_type = models.CharField(max_length=4, choices=[('INDI', 'Individual'), ('TEMP', 'Temporary')], default='')
    application_type = models.CharField(max_length=5, choices=[('NEW','New'), ('RENEW', 'Renewal'), ('REPLA', 'Replacement')], default='')
    reasons = models.CharField(max_length=4, choices=[('LOST', 'Lost'), ('STOL', 'Stolen'), ('DMAG', 'Damaged'), ('DFAC', 'Defaced'), ('CONF', 'Confiscated'), ('CHDE', 'Changed Details'), ('NORE',  'Non Receipt of Permit')], null=True)
    held_license = models.CharField(max_length=3, choices=[('Yes', 'Yes'), ('No', 'No')], default='')
    othername = models.CharField(max_length=20, null=True)
    current_license = models.CharField(max_length=3,  choices=[('Yes', 'Yes'), ('No', 'No')], default='')
    license_number = models.CharField(max_length=10, null=True)
    license_class = models.CharField(max_length=10, null=True)
    expiry_date = models.DateField(null=True)
    medical_review = models.CharField(max_length=3,  choices=[('Yes', 'Yes'), ('No', 'No')], default='')
    medical_condition =models.CharField(max_length=3,  choices=[('Yes', 'Yes'), ('No', 'No')], default='', null=True)
    disability = models.CharField(max_length=50, default='')
    temp_condition = models.CharField(max_length=10, default='')
    period =models.IntegerField(null=True)
    patient_years = models.CharField(max_length=4, default='')
    patient_months = models.CharField(max_length=2, default='')
    epilepsy = models.CharField(max_length=3,  choices=[('Yes', 'Yes'), ('No', 'No')], default='')
    epilepsy_date_onset = models.DateField(null=True)
    epilepsy_last_seizure = models.DateField(null=True)
    doctor_certificate = models.CharField(max_length=5, choices=[('Fit', 'Fit'), ('Unfit', 'Unfit')], default='')
    sectionTwo = models.CharField(max_length=6, choices=[('SUBMIT', 'Submitted'), ('NOSUB', 'Not submitted')], default='NOSUB')
    def __str__(self):
        return f"{self.application_id}" 
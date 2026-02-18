from django.shortcuts import render, redirect, get_object_or_404
from mps_application.models import Resident, MedicalPractitioner, Application
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required, permission_required
from django.core.validators import MaxLengthValidator, EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from datetime import datetime

#information page without login(seen by anyone)
def home(request):
    return render(request, "mps_application/homepage.html")

def logout_confirmation(request):
    return render(request, 'mps_application/logout.html')

@require_POST  
def logout_view(request):
    logout(request)  # Perform the logout
    return redirect('home')  # Redirect after logout

#condition page(seen by anyone)
def condition(request):
    return render(request, "mps_application/conditions.html")

#profile page after login
@login_required(login_url='login')
def profile(request):
    return render(request, 'mps_application/profile.html')


def validatelicense(licanse):
    licanse_validator = MaxLengthValidator(10, "Value is too long")
    try:
        licanse_validator(licanse)
    except ValidationError as e:
        error_message = str(e.message)
        return error_message

#application form for residents (section 1)
@login_required(login_url='login')
@transaction.atomic
def sectionOne(request):
    resident = get_object_or_404(Resident, user=request.user)
    current_date = datetime.now().date()
    
    if request.method == 'POST':
        errors = []
        permit_type = request.POST.get('permitType')
        application_type = request.POST.get('applicationType')
        held_license = request.POST.get('heldLicense')
        current_license = request.POST.get('currentLicense')
        medical_review = request.POST.get('medicalReview')
        medical_practitioner = None 
        medical_condition=None
        
        if not permit_type:
            errors.append('Permit type is required.')

        if not application_type:
            errors.append('Application type is required.')

        if not held_license:
            errors.append('License selection required.')
        
        if not current_license:
            errors.append('Current license status required.')
        
        if not medical_review:
            errors.append('Medical review status required.')
        
        selected_applicationtype = application_type
        reasons = request.POST.get('reasons', None)
        if selected_applicationtype == "REPL" and not reasons:
            errors.append('Reasons for replacement is required.')

        selected_heldlicense = held_license
        othername = request.POST.get('othername', None) 
        if selected_heldlicense == "Yes" and not othername:
            errors.append('Other name is required.')

        selected_currentlicense = current_license
        if selected_currentlicense == "Yes":
            license_number = request.POST.get('licenseNumber')
            if not license_number:
                errors.append('License number required.')
            else:
                validation_error = validatelicense(license_number)
                if validation_error:
                    errors.append(validation_error)
            license_class = request.POST.get('licenseClass')
            if not license_class:
                errors.append('License class is required.')
            else:
                validation_error = validatelicense(license_class)
                if validation_error:
                    errors.append(validation_error)
            expiry_date = request.POST.get('expiry')
            if not expiry_date:
                errors.append('Expiry date is required.')

        selected_medicalReview = medical_review
        if selected_medicalReview == "Yes":
            medical_condition = request.POST.get('medicalCondition')
            if not medical_condition:
                errors.append('Medical condition required.')

        if errors:
            return render(request, 'mps_application/sectionOne.html', {'errors': errors, 'current_date': current_date})

        try:
            application = Application(
                permit_type=permit_type,
                application_type=application_type,
                reasons=reasons,
                resident=resident,
                held_license=held_license,
                othername=othername,
                current_license=current_license,
                license_number=license_number,
                license_class=license_class,
                expiry_date=expiry_date,
                medical_review=medical_review,
                medical_condition=medical_condition,
                medical_practitioner =medical_practitioner,
                status='RR'
            )
            application.save()
        except Exception as e:
            errors.append(str(e))
            return render(request, 'mps_application/sectionOne.html', {'errors': errors, 'current_date': current_date})
        return redirect('profile')
    
    return render(request, 'mps_application/sectionOne.html', {'current_date': current_date})


#application form for MP (section 2)
@login_required(login_url='login')
def sectionTwo(request, application_id):
    application = get_object_or_404(Application, application_id=application_id)
    if application.sectionTwo == 'SUBMIT':
        return redirect('sectionThree', application_id=application_id)
    resident = application.resident
    medical_practitioner = get_object_or_404(MedicalPractitioner, user=request.user)
    current_date = datetime.now().date()

    if application.sectionTwo == 'SUBMIT':
                    return redirect('sectionThree', application_id=application_id)

    if request.method == 'POST':
        errors = []
        disability = request.POST.get('disability')
        temp_condition = request.POST.get('conditionTemp')
        period = request.POST.get('period')
        action = request.POST.get('action')

        if action == 'Save':
            application.disability = disability
            application.temp_condition=temp_condition
            application.period = period
            application.status='DR'
            application.save()
            return redirect('profile')
        
        elif action == 'Submit':
            if not disability:
                errors.append('Disability is required.')
            if not temp_condition:
                errors.append('Temporary condition is required.')
            selected_tempcondition = temp_condition
            if selected_tempcondition == "Yes" and not period:
                    errors.append('Period of disability is required.')
            if temp_condition == "isTemporary":
                try:
                    application.period = int(period)
                except ValueError:
                    errors.append('Period must be a valid number.')
            if application.medical_review == "No" or application.medical_condition == "Yes":
                status='RE'
            else:
                status='DR'
            if errors:
                return render(request, 'mps_application/sectionTwo.html', {
                    'errors': errors,
                    'application': application,
                    'resident': resident,
                    'medical_practitioner': medical_practitioner,
                    'current_date': current_date
                })
            try:
                application.disability=disability
                application.temp_condition=temp_condition
                application.period = period
                application.resident=resident
                application.medical_practitioner=medical_practitioner
                application.status=status
                application.sectionTwo = 'SUBMIT'
                application.save()
            except Exception as e:
                errors.append(str(e))
                return render(request, 'mps_application/sectionTwo.html', {'errors': errors,
                    'application':application, 
                    'resident':resident,
                    'medical_practitioner': medical_practitioner,
                    'current_date': current_date
                })
            if application.medical_review == "No" or application.medical_condition == "Yes":
                return redirect('sectionThree', application_id=application_id)   
            return redirect('profile')
        
    return render(request, 'mps_application/sectionTwo.html', {'application':application, 
        'resident':resident,
        'medical_practitioner': medical_practitioner,
        'current_date': current_date}
    )


#application form for MP (section 3)
@login_required(login_url='login')
def sectionThree(request, application_id):
    application = get_object_or_404(Application, application_id=application_id)
    if application.status == 'RE':
        return redirect('applications')
    resident = application.resident
    medical_practitioner = get_object_or_404(MedicalPractitioner, user=request.user)
    
    if request.method == 'POST':
        errors = []
        patient_years = request.POST.get('years')
        patient_months = request.POST.get('months')
        epilepsy = request.POST.get('Epilepsy')
        epilepsy_date_onset = request.POST.get('epilepsy-onset')
        epilepsy_last_seizure = request.POST.get('epilepsy-last-seizure')
        doctor_certificate = request.POST.get('Certification')
        action = request.POST.get('action')

        if action == 'Save':
            application.patient_years = patient_years
            application.patient_months = patient_months
            application.epilepsy = epilepsy
            application.epilepsy_date_onset = epilepsy_date_onset
            application.epilepsy_last_seizure = epilepsy_last_seizure
            application.doctor_certificate = doctor_certificate
            application.status='DR'
            application.save()
            return redirect('profile')
        
        elif action == 'Submit':
            if not patient_years:
                errors.append('Patient year is required.')
            if not patient_months:
                errors.append('Patient month is required.')
            if not epilepsy:
                errors.append('Epilepsy is required.')
            if not doctor_certificate:
                errors.append('Doctor certificate is required.')
            selected_epilepsy = epilepsy
            if selected_epilepsy == "Yes":
                if not epilepsy_date_onset:
                    errors.append('Date of onset is required.')
                if not epilepsy_last_seizure:
                    errors.append('Date of last seizure id required.')
            
            try:
                application.patient_years = patient_years
                application.patient_months = patient_months
                application.epilepsy = epilepsy
                application.epilepsy_date_onset = epilepsy_date_onset
                application.epilepsy_last_seizure = epilepsy_last_seizure
                application.doctor_certificate = doctor_certificate
                application.resident=resident
                application.medical_practitioner=medical_practitioner
                application.status='RE'
                application.save()
            except Exception as e:
                errors.append(str(e))
                print(f"Application submission failed: {e}")
                return render(request, 'mps_application/sectionThree.html', {'errors': errors, 
                    'application':application, 
                    'resident':resident,
                    'medical_practitioner': medical_practitioner,
                })
            return redirect('profile')
    
    return render(request, 'mps_application/sectionThree.html', {'application': application, 
        'resident':resident,
        'medical_practitioner': medical_practitioner,
    })


#application list for MP
def show_applicantion(request):
    if request.method == "GET":
        return render(request,
            'mps_application/applications.html',
            {"application": Application.objects.all(),
             "count": Application.objects.all().count(),
            }
        )
    else:
        selected_status = request.POST["status"]
        if selected_status == "all" or selected_status == "":
            return render(request,
                'mps_application/applications.html',
                {"application":Application.objects.all(),
                 "count": Application.objects.all().count(),
                }
            )
        else:
            return render(request,
                'mps_application/applications.html',
                {"application": Application.objects.filter(status=selected_status),
                "count": Application.objects.filter(status=selected_status).count(),
                }
            )    

def validatename(aname):
    name_validator = MaxLengthValidator(15, "Value is too long")
    try:
        name_validator(aname)
    except ValidationError as e:
        error_message = str(e.message)
        return error_message

def validateemail(email):
    email_validator = EmailValidator()
    try:
        email_validator(email)
    except ValidationError as e:
        error_message = str(e.message)
        return error_message

def validateaddress(address):
    address_validator = MaxLengthValidator(200, "Value is too long")
    try:
        address_validator(address)
    except ValidationError as e:
        error_message = str(e.message)
        return error_message

def validatepostcode(postal_code):
    postcode_validator = MaxLengthValidator(4, "Value is too long")
    try:
        postcode_validator(postal_code)
    except ValidationError as e:
        error_message = str(e.message)
        return error_message
    
def validatephone(phone_number):
    phone_validator = MaxLengthValidator(15, "Value is too long")
    try:
        phone_validator(phone_number)
    except ValidationError as e:
        error_message = str(e.message)
        return error_message


#registration form(seen by anyone)
@transaction.atomic
def create_user(request):
    if request.method == 'POST':
        errors = []
        #Get form data from the POST request
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        address = request.POST['address']
        postal_code = request.POST['postal-code']
        phone_number = request.POST['primary-phone']
        date_of_birth = request.POST['dob']
        password = request.POST.get('password')

        #Validate the form data
        if not first_name:
            errors.append('First name is required.')
        else:
            validation_error = validatename(first_name)
            if validation_error:
                errors.append(validation_error)

        if not last_name:
            errors.append('Last name is required.')
        else:
            validation_error = validatename(last_name)
            if validation_error:
                errors.append(validation_error)
        
        if not email:
            errors.append('Email is required.')
        else:
            validation_error = validateemail(email)
            if User.objects.filter(email=email).exists():
                errors.append('Email is already registered.')
            if validation_error:
                errors.append(validation_error)

        if not address:
            errors.append('Address is required.')
        else:
            validation_error = validateaddress(address)
            if validation_error:
                errors.append(validation_error)

        if not postal_code:
            errors.append('Postal code is required.')
        else:
            validation_error = validatepostcode(postal_code)
            if validation_error:
                errors.append(validation_error)

        if not phone_number:
            errors.append('Phone number is required.')
        else:
            validation_error = validatephone(phone_number)

        if not date_of_birth:
            errors.append('Date of Birth is required.')

        if not password:
            errors.append('Password is required.')

        if errors:
            return render(request, 'mps_application/Registration.html', {'errors': errors})
        
        try:
            user = User.objects.create_user(
                username=email, 
                first_name=first_name, 
                last_name=last_name, 
                email=email,
                password=password,
                is_active=True
            )
        except Exception as e:
            errors.append(str(e))
            print(f"User creation failed: {e}")
            return render(request, 'mps_application/Registration.html', {'errors': errors})
        
        #Create a new User object
        new_user = Resident(
            user=user,
            address=address,
            postal_code=postal_code,
            date_of_birth=date_of_birth,
            phone_number=phone_number,        
        )

        try:
            new_user.save()
        except Exception as e:
            errors.append(str(e))
            print(f"User creation failed: {e}")
            return render(request, 'mps_application/Registration.html', {'errors': errors})
        return redirect('profile')
    
    return render(request, 'mps_application/Registration.html')
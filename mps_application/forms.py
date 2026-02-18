from django import forms

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, label='First Name')
    middle_name = forms.CharField(max_length=100, required=False, label='Middle Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    address = forms.CharField(max_length=255, label='Residential Address')
    city = forms.CharField(max_length=100, label='City/Suburb')
    state = forms.CharField(max_length=100, label='State')
    postal_code = forms.CharField(max_length=10, label='Postal Code')
    country = forms.CharField(max_length=100, label='Country')
    primary_phone = forms.CharField(max_length=15, label='Primary Contact Phone Number')
    secondary_phone = forms.CharField(max_length=15, required=False, label='Secondary Contact Phone Number (optional)')
    email = forms.EmailField(max_length=100, label='Email Address')
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label='Date of Birth')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('non-binary', 'Non-binary'), ('prefer-not-to-say', 'Prefer not to say')], label='Gender')
    communication_support = forms.ChoiceField(choices=[('no', 'No'), ('large-print', 'Large Print'), ('braille', 'Braille'), ('sign-language', 'Sign Language Interpreter'), ('other', 'Other')], label='Do you require communication support?')
    other_support = forms.CharField(max_length=255, required=False, label='If other, please specify')

    condition = forms.ChoiceField(choices=[('yes', 'Yes'), ('no', 'No')], label='Do you have a medical condition or disability that impacts your mobility or vision?')
    condition_details = forms.CharField(widget=forms.Textarea, required=False, label='If Yes, please briefly describe your condition(s)')

    emergency_contact_name = forms.CharField(max_length=100, label='Full Name of Emergency Contact')
    relationship = forms.ChoiceField(choices=[('spouse', 'Spouse'), ('parent', 'Parent'), ('child', 'Child'), ('sibling', 'Sibling'), ('friend', 'Friend'), ('carer', 'Carer'), ('other', 'Other')], label='Relationship to Resident')
    emergency_phone = forms.CharField(max_length=15, label='Emergency Contact Phone Number')
    emergency_email = forms.EmailField(required=False, label='Emergency Contact Email Address')

    preferred_contact = forms.ChoiceField(choices=[('phone', 'Phone Call'), ('sms', 'SMS/Text Message'), ('email', 'Email')], label='Preferred Contact Method')
    hear_about = forms.ChoiceField(choices=[('website', 'Website'), ('social-media', 'Social Media'), ('friend', 'Friend/Family'), ('medical', 'Medical Practitioner'), ('other', 'Other')], label='How did you hear about the Mobility Parking Scheme (MPS)?')

    acknowledgment = forms.BooleanField(label="I confirm that the information provided is accurate and complete to the best of my knowledge.")
    consent = forms.BooleanField(label="I consent to the Southern Coastland Roads Authority collecting and using my personal information for the purpose of processing my application for an MPS permit.")
    electronic_communication = forms.BooleanField(label="I agree to receive communications electronically regarding my application and permit status.")


class SectionOneForm(forms.Form):
    permit_type = forms.ChoiceField(
        choices=[('individual', 'Individual'), ('temporary', 'Temporary')],
        widget=forms.RadioSelect,
        label="Type of MPS permit needed"
    )

    application_type = forms.ChoiceField(
        choices=[('new', 'New'), ('renewal', 'Renewal'), ('replacement', 'Replacement')],
        widget=forms.RadioSelect,
        label="Type of Application"
    )

    reasons = forms.ChoiceField(
        choices=[('lost', 'Lost'), ('stolen', 'Stolen'), ('damaged', 'Damaged Permit'), ('defaced', 'Defaced Permit'), ('confiscated', 'Confiscated Permit'), ('changedDetails', 'Changed Details'), ('nonReceipt', 'Non Receipt of Permit')],
        widget=forms.Select,
        label="Reason for Replacement",
        required=False  # Only required if "Replacement" is selected
    )

    applicant_name = forms.CharField(
        label="Applicant Name",
        initial="John Doe",
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    residential_address = forms.CharField(
        label="Residential Address",
        initial="123 Main St, Sydney, NSW",
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    date_of_birth = forms.DateField(
        label="Date of Birth",
        initial="1990-01-01",
        widget=forms.DateInput(attrs={'readonly': 'readonly'})
    )
    customer_number = forms.IntegerField(
        label="Customer No.",
        initial=12345,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )

    held_license = forms.ChoiceField(
        choices=[('No', 'No'), ('Yes', 'Yes')],
        widget=forms.RadioSelect,
        label="Do you hold or have you ever held a license?"
    )
    other_name = forms.CharField(
        label="Other Name (if applicable)",
        required=False
    )

    current_license = forms.ChoiceField(
        choices=[('No', 'No'), ('Yes', 'Yes')],
        widget=forms.RadioSelect,
        label="Do you hold a current or suspended NSW license?"
    )
    license_number = forms.CharField(
        label="License Number",
        required=False
    )
    license_class = forms.CharField(
        label="License Class",
        required=False
    )
    expiry_date = forms.DateField(
        label="Expiry Date",
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    medical_review = forms.ChoiceField(
        choices=[('No', 'No'), ('Yes', 'Yes')],
        widget=forms.RadioSelect,
        label="Your license is subject to medical review?"
    )
    medical_condition = forms.ChoiceField(
        choices=[('No', 'No'), ('Yes', 'Yes')],
        widget=forms.RadioSelect,
        label="Do you have an additional medical condition to report?"
    )

    agree_submission = forms.BooleanField(
        required=True,
        label="I declare that the details in this application are true and complete."
    )
    declaration_date = forms.DateField(
        initial="2024-10-11",  
        widget=forms.HiddenInput(),
    )


class SectionTwoForm(forms.Form):
    disability_choices = [
        ('paraplegia', 'Paraplegia'),
        ('quadriplegia', 'Quadriplegia'),
        ('legAmputation', 'Leg amputation'),
        ('motorNeuron', 'Motor Neuron disease'),
        ('cerebralPalsy', 'Cerebral palsy'),
        ('chromosalOrSyndromic', 'Chromosomal or syndromic conditions'),
        ('neuroDegnerative', 'Neuro degenerative disorder'),
        ('neuroMascular', 'Neuro muscular disorder'),
        ('blindness', 'Blindness'),
        ('other', 'Other'),
    ]
    
    disability = forms.ChoiceField(
        choices=disability_choices,
        label="Select one of the clinically recognisable disabilities",
        widget=forms.Select(attrs={'onblur': 'validateField(this);'}),
        required=True
    )

    other_disability = forms.CharField(
        label="Other, please specify",
        required=False,
        widget=forms.TextInput(attrs={'onblur': 'validateOtherField();'}),
    )

    condition_temp = forms.ChoiceField(
        choices=[('isTemporary', 'Yes'), ('notTemporary', 'No')],
        label="Is the condition temporary?",
        widget=forms.RadioSelect(attrs={'onblur': 'validateCondition();'}),
        required=True
    )

    period = forms.IntegerField(
        label="If yes, give period of disability (in months)",
        required=False,
        widget=forms.NumberInput(attrs={
            'onblur': 'validatePeriodField(this);',
            'onchange': 'validateNumber(this, errorMonth, months);'
        })
    )

    agree_declaration = forms.BooleanField(
        label="I declare that the details in this application are true and complete.",
        widget=forms.CheckboxInput(attrs={'onchange': 'errorCheckBox(this)'}),
        required=True
    )

    agree_submission = forms.BooleanField(
        label="I certify that I have examined the person and they are a person with a disability.",
        widget=forms.CheckboxInput(attrs={'onchange': 'errorCheckBox(this)'}),
        required=True
    )


class SectionThreeForm(forms.Form):
    permit_reason = forms.ChoiceField(
        choices=[('urgent', 'Urgent Mobility Requirement'), ('health', 'Health Reason')],
        widget=forms.RadioSelect(),
        label="Reason for the urgency"
    )

    medical_condition = forms.CharField(
        label="Relevant Medical Condition",
        widget=forms.Textarea(attrs={'rows': 5}),
        required=False
    )

    previous_permit = forms.ChoiceField(
        choices=[('yes', 'Yes'), ('no', 'No')],
        widget=forms.RadioSelect(),
        label="Have you held a permit previously?"
    )

    declaration_date = forms.DateField(
        label="Date of Declaration",
        widget=forms.DateInput(attrs={'type': 'date', 'value': '2024-10-11'})
    )

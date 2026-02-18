// Validate history section
function validateHistory() {
    var yearsInput = document.getElementById("years");
    var monthsInput = document.getElementById("months");
    var historySection = document.querySelector(".history");
    var yearsError = document.getElementById("years-error");
    var monthsError = document.getElementById("months-error");

    // Clear previous errors
    yearsInput.style.border = "";
    monthsInput.style.border = "";
    historySection.style.border = "";
    yearsError.textContent = "";
    monthsError.textContent = "";

    // Check if years and months are filled
    if (yearsInput.value.trim() === "" || monthsInput.value.trim() === "") {
        historySection.style.border = "2px solid red";
        return false;
    }

    // Check if years and months are numbers and non-negative
    var yearsValue = parseInt(yearsInput.value);
    var monthsValue = parseInt(monthsInput.value);
    if (isNaN(yearsValue) || yearsValue < 0) {
        yearsInput.style.border = "2px solid red";
        yearsError.textContent = "Please enter a number";
        return false;
    }
    if (isNaN(monthsValue) || monthsValue < 0) {
        monthsInput.style.border = "2px solid red";
        monthsError.textContent = "Please enter a number";
        return false;
    }

    return true;
}

// Validate epilepsy section
function validateEpilepsy() {
    var epilepsyResponse = document.querySelector('input[name="Epilepsy"]:checked');
    var epilepsySection = document.querySelector(".epilepsy");

    // Clear previous errors
    epilepsySection.style.border = "";

    // Check if yes or no is selected
    if (!epilepsyResponse) {
        epilepsySection.style.border = "2px solid red";
        return false;
    } else {
        epilepsySection.style.border = "none";
    }

    return true;
}

// Validate doctor's certification section
function validateCertification() {
    var certificationResponse = document.querySelector('input[name="Certification"]:checked');
    var certificationSection = document.querySelector(".certification");

    // Clear previous errors
    certificationSection.style.border = "";

    // Check if yes or no is selected
    if (!certificationResponse) {
        certificationSection.style.border = "2px solid red";
        return false;
    } else {
        certificationSection.style.border = "none";
    }

    return true;
}

// Validate doctor's information section
function validateDoctorInfo() {
    var doctorNameField = document.getElementById("doctor-name");
    var providerNumberField = document.getElementById("provider-number");
    var phoneNumberField = document.getElementById("phone-number");

    // Clear previous errors
    doctorNameField.style.border = "";
    providerNumberField.style.border = "";
    phoneNumberField.style.border = "";

    // Check if doctor's name, provider number, and phone number are filled
    if (!doctorNameField.value.trim()) {
        doctorNameField.style.border = "2px solid red";
        return false;
    } else {
        doctorNameField.style.border = "none";
    }

    if (!providerNumberField.value.trim()) {
        providerNumberField.style.border = "2px solid red";
        return false;
    } else {
        providerNumberField.style.border = "none";
    }

    if (!phoneNumberField.value.trim()) {
        phoneNumberField.style.border = "2px solid red";
        return false;
    } else {
        phoneNumberField.style.border = "none";
    }

    return true;
}

// Validate the entire form
function validateForm() {
    var valid = false;
    if (!validateHistory()) valid = false;
    if (!validateEpilepsy()) valid = false;
    if (!validateCertification()) valid = false;
    if (!validateDoctorInfo()) valid = false;
    return valid;
}

// Call the validateForm function when the form is submitted
var form = document.querySelector('form');
form.addEventListener('submit', function(event) {
    if (!validateForm()) {
        event.preventDefault();
    }
});

// Function to display information
function displayInformation(){
    document.getElementById('doctor-name').value = "from database";
    document.getElementById('provider-number').value = "from database";
    document.getElementById('phone-number').value = "from database";
}

// Call the function directly
displayInformation();
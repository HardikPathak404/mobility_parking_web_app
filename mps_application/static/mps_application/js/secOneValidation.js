function setErrorStyle(input, label) {
    input.style.border = "1px solid red";
    label.style.color = "red";
}


function setErrorLabel(label) {
    label.style.color = "red";
}


function setErrorInput(input) {
    input.style.border = "1px solid red"
}


function validatePermitType() {
    var permitType = document.querySelector('input[name="permitType"]:checked');
    if (!permitType) {
        var label = document.querySelector('label[for="individual"]');
        setErrorLabel(label);
        return false;
    }
    return true;
}

function validateApplicationType() {
    var applicationType = document.querySelector('input[name="applicationType"]:checked');
    if (!applicationType) {
        var label = document.querySelector('label[for="new"]');
        setErrorLabel(label);
        return false;
    }

    // Validate reason for replacement if 'replacement' is chosen
    if (applicationType.value === "replacement") {
        var reason = document.getElementById("reasons");
        var label = document.querySelector('label[for="reasons"]');
        if (reason.value === "") {
            setErrorInput(reason);
            setErrorLabel(label);
            return false;
        }
    }
    return true;
}

function validateLicenseInfo() {
    var heldLicense = document.querySelector('input[name="heldLicense"]:checked');
    var currentLicense = document.querySelector('input[name="currentLicense"]:checked');
    
    if (!heldLicense) {
        var label = document.querySelector('label[for="noHeldLicense"]');
        setErrorLabel(label);
        return false;
    }
    
    // If "Yes" is selected for heldLicense, the accompanying text field must be filled
    if (heldLicense.value === "Yes") {
        var otherName = document.querySelector('input[name="heldLicense"] + input[type="text"]');
        if (otherName.value.trim() === "") {
            setErrorStyle(otherName, document.querySelector('label[for="yesHeldLicense"]'));
            return false;
        }
    }

    if (!currentLicense) {
        var label = document.querySelector('label[for="noCurrent"]');
        setErrorLabel(label);
        return false;
    }

    // If "Yes" is selected for currentLicense, validate License Number, License Class, and Expiry Date
    if (currentLicense.value === "Yes") {
        var licenseNumber = document.getElementById("licenseNumber").value.trim();
        var licenseClass = document.getElementById("licenseClass").value.trim();
        var expiryDate = document.getElementById("expiry").value;

        if (licenseNumber === "" || licenseClass === "" || expiryDate === "") {
            setErrorStyle(document.getElementById("licenseNumber"), document.querySelector('label[for="licenseNumber"]'));
            setErrorStyle(document.getElementById("licenseClass"), document.querySelector('label[for="licenseClass"]'));
            setErrorStyle(document.getElementById("expiry"), document.querySelector('label[for="expiry"]'));
            return false;
        }
    }
    
    return true;
}


function validateReplacementReason() {
    var applicationType = document.querySelector('input[name="applicationType"]:checked');
    if (applicationType && applicationType.value === "replacement") {
        var reasons = document.getElementById("reasons");
        if (reasons.value === "") {
            setErrorStyle(reasons, document.querySelector('label[for="reasons"]'));
            return false;
        }
    }
    return true;
}
//change the color to red if declaration and aggrement checkbox is not checked.
function errorCheckBox(checkBox){
    if (checkBox.checked){
        checkBox.labels[0].style.color = "black";
    } else{
        checkBox.labels[0].style.color = "red";
    }
}

//check if the checkbox has checked
function noCheckboxSelected (checkBoxGroup){
    for(var i=0; i<checkBoxGroup.length; i++) {
        if(checkBoxGroup[i].checked) {
            return false;
        }
    }
    return true;
}



function displayInformation(){
    document.getElementById('surname').innerHTML = "from database";
    document.getElementById('givenNames').innerHTML = "from database";
    document.getElementById('address').innerHTML = "from database";
    document.getElementById('date').innerHTML = "from database";
    document.getElementById('customer').innerHTML = "from database";
}





function validateForm(theForm) {
    var valid = true;
    // Validate each section of the form
    /*var isPermitTypeValid = validatePermitType();
    var isApplicationTypeValid = validateApplicationType();
    var isLicenseInfoValid = validateLicenseInfo();
    var isDeclarationValid = validateDeclaration();
    var isReplacementReasonValid = validateReplacementReason();

    // Check if all validations passed
    if (isPermitTypeValid == false || isApplicationTypeValid == false || isLicenseInfoValid == false || isDeclarationValid == false || isReplacementReasonValid == false) {
        valid = false; // Prevent form submission if any validation fails
    }else {
        valid = true;
    }*/


    var permitType = document.querySelector('input[name="permitType"]:checked');
    if (!permitType) {
        var label = document.querySelector('label[for="individual"]');
        setErrorLabel(label);
        return valid = false;
        }




    var applicationType = document.querySelector('input[name="applicationType"]:checked');
    if (!applicationType) {
        var label = document.querySelector('label[for="new"]');
        setErrorLabel(label);
        return valid = false;
        }

        // Validate reason for replacement if 'replacement' is chosen
        if (applicationType.value === "replacement") {
            var reason = document.getElementById("reasons");
            var label = document.querySelector('label[for="reasons"]');
            if (reason.value === "") {
                setErrorInput(reason);
                setErrorLabel(label);
                return valid = false;
            }
        }
       // return true;


var heldLicense = document.querySelector('input[name="heldLicense"]:checked');
    var currentLicense = document.querySelector('input[name="currentLicense"]:checked');
    
    if (!heldLicense) {
        var label = document.querySelector('label[for="noHeldLicense"]');
        setErrorLabel(label);
        return valid = false;
    }
    
    // If "Yes" is selected for heldLicense, the accompanying text field must be filled
    if (heldLicense.value === "Yes") {
        var otherName = document.querySelector('input[name="heldLicense"] + input[type="text"]');
        if (otherName.value.trim() === "") {
            setErrorStyle(otherName, document.querySelector('label[for="yesHeldLicense"]'));
            return valid = false;
        }
    }

    if (!currentLicense) {
        var label = document.querySelector('label[for="noCurrent"]');
        setErrorLabel(label);
        return valid = false;
    }

    // If "Yes" is selected for currentLicense, validate License Number, License Class, and Expiry Date
    if (currentLicense.value === "Yes") {
        var licenseNumber = document.getElementById("licenseNumber").value.trim();
        var licenseClass = document.getElementById("licenseClass").value.trim();
        var expiryDate = document.getElementById("expiry").value;

        if (licenseNumber === "" || licenseClass === "" || expiryDate === "") {
            setErrorStyle(document.getElementById("licenseNumber"), document.querySelector('label[for="licenseNumber"]'));
            setErrorStyle(document.getElementById("licenseClass"), document.querySelector('label[for="licenseClass"]'));
            setErrorStyle(document.getElementById("expiry"), document.querySelector('label[for="expiry"]'));
            return valid = false;
        }
    }
    
   // return true;

    var applicationType = document.querySelector('input[name="applicationType"]:checked');
    if (applicationType && applicationType.value === "replacement") {
        var reasons = document.getElementById("reasons");
        if (reasons.value === "") {
            setErrorStyle(reasons, document.querySelector('label[for="reasons"]'));
            return valid = false;
        }
    }
    //return true;


    // Validate checkboxes
    if (noCheckboxSelected(theForm.agreeSubmission)) {
        valid = false;
        document.getElementById('submissionAgreed').style.color = "red";  
    }else{
        document.getElementById('submissionAgreed').style.color = "black";
        valid = true;
    }

    // Validate submissionDate
    if (!theForm.submissionDate.value.length) {
        valid = false;
        //theForm.submissionDate.labels[0].style.color = "red";
        theForm.submissionDate.style.border = "1px solid red";
    } else {
        //theForm.submissionDate.labels[0].style.color = "black";
        theForm.submissionDate.style.border = "1px solid #ccc";
        valid = true;
    }


    return valid;

}

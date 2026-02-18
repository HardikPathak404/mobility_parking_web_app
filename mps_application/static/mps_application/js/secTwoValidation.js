//validate input data type
function validateNumber(obj, msg, unit){
    var userInput = obj.value;
    var isTemporarySelected = document.getElementById("isTemporary").checked;
        if(isTemporarySelected){
            if(userInput.length != 0){
                if(isNaN(userInput)){
                msg.innerHTML = "Number only.";
                } else if(userInput > 6){
                msg.innerHTML = "The period must be 6 or below.";
                } else if(userInput < 0){
                msg.innerHTML = "The period cannot be negative.";
                } else{
                msg.innerHTML = "";
                }
            if (msg.innerHTML != "") {
                msg.style.border = "1px solid red";
                msg.style.color = "red";
                obj.style.border = "1px solid red";
                unit.style.color = "red";
            } else {
                obj.style.border = "1px solid #ccc";
                unit.style.color = "black";
            }
        }
    }
    return;
}

//check the period field if the asnwer of the temporary condition is 'yes'
function validatePeriodField(element){
    var period = element.value
    var conditionTemporary = document.querySelector('input[name="conditionTemp"]:checked').value;
    if(period.length == 0 && conditionTemporary == "isTemporary"){
        element.labels[0].style.color = "red";
        element.style.border = "1px solid red";
        document.getElementById('months').style.color = 'red';
    } else {
        element.labels[0].style.color = "black";
        element.style.color = "1px solid black";
        document.getElementById('months').style.color = 'black';
    }
}

//return true if the number is not valid
function notValidNumber(obj){
    var inputNumber = obj.value;
    if(inputNumber.length != 0){
        if(isNaN(inputNumber)){
            return true;
        }
        else if(inputNumber > 6){
            return true;
        }
        else if(inputNumber < 0){
            return true;
        }
        else
            return false;
    }
}

function validateCondition(){
    var conditionTemporary = document.querySelector('input[name="conditionTemp"]:checked');
    if(!conditionTemporary){
        document.getElementById('isTemporary_label').style.color = "red";
        document.getElementById('notTemporary_label').style.color = "red";
    } else {
        document.getElementById('isTemporary_label').style.color = "black";
        document.getElementById('notTemporary_label').style.color = "black";
    }
}

function validateField(element){
    if(!element.value.length){
        if(element.labels && element.labels.length > 0){
            element.labels[0].style.color = "red"; 
        }
        if(element.style){
            element.style.border = "1px solid red";
        }
    } else {
        if(element.labels && element.labels.length > 0){
            element.labels[0].style.color = "black"; 
        }
        if(element.style){
            element.style.border = "1px solid #ccc";
        }
    }
}

//check if the other disability is written if practitioner selects 'other'
function validateOtherField(){
    var selectedElement = document.getElementById('disability');
    var otherDescription = document.getElementById('otherDisability');
    if (selectedElement.value == "other" && !otherDescription.value.length){
            document.getElementById('otherDisability_label').style.color = "red";
            otherDescription.style.border = "1px solid red";
            otherDescription.style.color = "red";
    } else{
        document.getElementById('otherDisability_label').style.color = "black";
        otherDescription.style.border = "1px solid #ccc";
        otherDescription.style.color = "black";
    }
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


//validate all the fields are filled to submit the form
function validateTheForm(theForm){
    var valid = true; 
    var selectedElement = theForm.disability;
    var otherDescription = theForm.otherDisability;
    var conditionTemporary = document.querySelector('input[name="conditionTemp"]:checked');

    // Validate the disability and otherDisability fields
    if(!selectedElement.value.length){
        valid = false;
        document.getElementById('disability_label').style.color = "red"; 
    } else if (selectedElement.value == "other" && !otherDescription.value.length) {
        valid = false;
        otherDescription.style.border = "1px solid red";
        otherDescription.style.color = "red";
    } else {
        document.getElementById('disability_label').style.color = "black";
        otherDescription.style.border = "1px solid #ccc";
        otherDescription.style.color = "black";
        valid = true;
    }

    // Validate the period field if temporary condition checked
    if(!conditionTemporary){
        valid = false;
        document.getElementById('isTemporary_label').style.color = "red";
        document.getElementById('notTemporary_label').style.color = "red";
    } else if (conditionTemporary && conditionTemporary.value == "isTemporary") {
        if (!theForm.period.value.length || notValidNumber(theForm.period)) {
            valid = false;
            theForm.period.labels[0].style.color = "red";
            theForm.period.style.border = "1px solid red";
        }
    } else {
        document.getElementById('isTemporary_label').style.color = "black";
        document.getElementById('notTemporary_label').style.color = "black";
        theForm.period.labels[0].style.color = "black";
        theForm.period.style.border = "1px solid #ccc";
        valid = true;
    }

    // Validate checkboxes
    if (noCheckboxSelected(theForm.agreeDeclaration)) {
        valid = false;
        document.getElementById('agreeDeclaration_label').style.color = "red";  
    }else{
        document.getElementById('agreeDeclaration_label').style.color = "black";  
        valid = true;
    }

    if (noCheckboxSelected(theForm.agreeSubmission)) {
        valid = false;
        document.getElementById('agreeSubmission_label').style.color = "red";  
    }else{
        document.getElementById('agreeSubmission_label').style.color = "black";
        valid = true;
    }

    // Validate submissionDate
    if (!theForm.submissionDate.value.length) {
        valid = false;
        theForm.submissionDate.labels[0].style.color = "red";
        theForm.submissionDate.style.border = "1px solid red";
    } else {
        theForm.submissionDate.labels[0].style.color = "black";
        theForm.submissionDate.style.border = "1px solid #ccc";
        valid = true;
    }

    return valid;
}

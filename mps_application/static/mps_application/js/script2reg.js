function validateForm() {
    let valid = true;

    
    const firstName = document.getElementById('first-name').value.trim();
    const lastName = document.getElementById('last-name').value.trim();
    const address = document.getElementById('address').value.trim();
    const primaryPhone = document.getElementById('primary-phone').value.trim();
    const email = document.getElementById('email').value.trim();
    const dob = document.getElementById('dob').value;
    const password = document.getElementById('password').value;

    const acknowledgment = document.getElementById('acknowledgment').checked;
    const consent = document.getElementById('consent').checked;
    const electronicCommunication = document.getElementById('electronic-communication').checked;

    
    document.getElementById('first-name-error').textContent = '';
    document.getElementById('last-name-error').textContent = '';
    document.getElementById('address-error').textContent = '';
    document.getElementById('primary-phone-error').textContent = '';
    document.getElementById('email-error').textContent = '';
    document.getElementById('dob-error').textContent = '';
    document.getElementById('password-error').textContent = '';
    document.getElementById('acknowledgment-error').textContent = '';
    document.getElementById('consent-error').textContent = '';
    document.getElementById('electronic-communication-error').textContent = '';

    // Validation logic
    if (firstName === "") {
        document.getElementById('first-name-error').textContent = 'First Name should not be empty.';
        valid = false;
    }

    if (lastName === "") {
        document.getElementById('last-name-error').textContent = 'Last Name should not be empty.';
        valid = false;
    }

    if (address === "") {
        document.getElementById('address-error').textContent = 'Address should not be empty.';
        valid = false;
    }

    if (primaryPhone.length !== 10 || !(primaryPhone.startsWith('04') || primaryPhone.startsWith('02'))) {
        document.getElementById('primary-phone-error').textContent = 'Phone number must be 10 digits and start with 04 or 02.';
        valid = false;
    }

    if (!email.includes('@') || !email.includes('.')) {
        document.getElementById('email-error').textContent = 'Please enter a valid email address.';
        valid = false;
    }

    if (dob === "" || isNaN(new Date(dob))) {
        document.getElementById('dob-error').textContent = 'Please enter a valid date of birth.';
        valid = false;
    }

    if (!password) {
        document.getElementById('password-error').textContent = 'Please enter a password.';
        valid = false;

    if (!acknowledgment) {
        document.getElementById('acknowledgment-error').textContent = 'You must acknowledge that the information provided is accurate.';
        valid = false;
    }

    if (!consent) {
        document.getElementById('consent-error').textContent = 'You must provide consent to collect and use your personal information.';
        valid = false;
    }

    if (!electronicCommunication) {
        document.getElementById('electronic-communication-error').textContent = 'You must agree to receive communications electronically.';
        valid = false;
    }

    return valid;
}

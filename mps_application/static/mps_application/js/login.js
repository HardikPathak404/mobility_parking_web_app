function validateTheForm(theForm){
    var valid = true; 
    var username = theForm.username;
    var password = theForm.password;

    if(!username.value.length){
        valid = false;
        document.getElementById('username_label').style.color = "red"; 
        username.style.border = "1px solid red";
    } else {
        document.getElementById('username_label').style.color = "black";
        username.style.border = "1px solid #ccc";
    }

    if(!password.value.length){
        valid = false;
        document.getElementById('password_label').style.color = "red"; 
        password.style.border = "1px solid red";
    } else {
        document.getElementById('password_label').style.color = "black";
        password.style.border = "1px solid #ccc";
    }

    return valid;
}
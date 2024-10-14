// static/js/registration_validation.js

document.addEventListener('DOMContentLoaded', function () {
    const password = document.querySelector('input[name="password"]');
    const confirmPassword = document.querySelector('input[name="confirm_password"]');
    const passwordMatchCriteria = document.getElementById('password-match');

    function validatePasswordMatch() {
        if (password.value === confirmPassword.value) {
            passwordMatchCriteria.style.color = 'green';
            passwordMatchCriteria.textContent = 'Passwords match';
        } else {
            passwordMatchCriteria.style.color = 'red';
            passwordMatchCriteria.textContent = 'Passwords do not match';
        }
    }

    password.addEventListener('input', validatePasswordMatch);
    confirmPassword.addEventListener('input', validatePasswordMatch);
});
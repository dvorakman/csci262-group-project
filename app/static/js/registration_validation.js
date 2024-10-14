// static/js/registration_validation.js

document.addEventListener('DOMContentLoaded', function () {
    const password = document.querySelector('input[name="password"]');
    const confirmPassword = document.querySelector('input[name="confirm_password"]');
    const emailInput = document.querySelector('input[name="email"]');
    const criteria = {
        uppercase: document.getElementById('uppercase'),
        lowercase: document.getElementById('lowercase'),
        digit: document.getElementById('digit'),
        special: document.getElementById('special'),
        noSpaces: document.getElementById('no-spaces'),
        minLength: document.getElementById('min-length'),
        passwordMatch: document.getElementById('password-match'),
        emailValidity: document.getElementById('email-validity')
    };

    function validatePasswordMatch() {
        if (password.value === confirmPassword.value) {
            criteria.passwordMatch.style.color = 'green';
            criteria.passwordMatch.textContent = 'Passwords match';
        } else {
            criteria.passwordMatch.style.color = 'red';
            criteria.passwordMatch.textContent = 'Passwords do not match';
        }
    }

    function validatePasswordCriteria() {
        const passwordValue = password.value;
        criteria.uppercase.style.color = /[A-Z]/.test(passwordValue) ? 'green' : 'red';
        criteria.lowercase.style.color = /[a-z]/.test(passwordValue) ? 'green' : 'red';
        criteria.digit.style.color = /\d/.test(passwordValue) ? 'green' : 'red';
        criteria.special.style.color = /[!@#$%^&*(),.?":{}|<>]/.test(passwordValue) ? 'green' : 'red';
        criteria.noSpaces.style.color = /\s/.test(passwordValue) ? 'red' : 'green';
        criteria.minLength.style.color = passwordValue.length >= 8 ? 'green' : 'red';
    }

    function validateEmail() {
        const emailValue = emailInput.value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        criteria.emailValidity.style.color = emailPattern.test(emailValue) ? 'green' : 'red';
    }

    password.addEventListener('input', function() {
        validatePasswordCriteria();
        validatePasswordMatch();
    });

    confirmPassword.addEventListener('input', validatePasswordMatch);
    emailInput.addEventListener('input', validateEmail);
});
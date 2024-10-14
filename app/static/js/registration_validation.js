// static/js/password_validation.js
document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.querySelector('input[name="password"]');
    const emailInput = document.querySelector('input[name="email"]');
    const criteria = {
        uppercase: document.getElementById('uppercase'),
        lowercase: document.getElementById('lowercase'),
        digit: document.getElementById('digit'),
        special: document.getElementById('special'),
        noSpaces: document.getElementById('no-spaces'),
        minLength: document.getElementById('min-length'),
        emailValidity: document.getElementById('email-validity')
    };

    passwordInput.addEventListener('input', function() {
        const password = passwordInput.value;
        criteria.uppercase.style.color = /[A-Z]/.test(password) ? 'green' : 'red';
        criteria.lowercase.style.color = /[a-z]/.test(password) ? 'green' : 'red';
        criteria.digit.style.color = /\d/.test(password) ? 'green' : 'red';
        criteria.special.style.color = /[!@#$%^&*(),.?":{}|<>]/.test(password) ? 'green' : 'red';
        criteria.noSpaces.style.color = /\s/.test(password) ? 'red' : 'green';
        criteria.minLength.style.color = password.length >= 8 ? 'green' : 'red';
    });

    emailInput.addEventListener('input', function() {
        const email = emailInput.value;
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        criteria.emailValidity.style.color = emailPattern.test(email) ? 'green' : 'red';
    });
});
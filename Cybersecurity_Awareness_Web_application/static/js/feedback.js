document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const feedbackInput = document.getElementById('feedback');
    const submitButton = document.querySelector('button[type="submit"]');

    // Add event listener for form submission
    form.addEventListener('submit', (event) => {
        if (!validateForm()) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });

    // Validate form fields
    function validateForm() {
        let isValid = true;

        // Clear previous errors
        clearErrors();

        if (!nameInput.value.trim()) {
            showError(nameInput, 'Name is required.');
            isValid = false;
        }

        if (!validateEmail(emailInput.value)) {
            showError(emailInput, 'Please enter a valid email address.');
            isValid = false;
        }

        if (!feedbackInput.value.trim()) {
            showError(feedbackInput, 'Feedback cannot be empty.');
            isValid = false;
        }

        return isValid;
    }

    // Validate email address format
    function validateEmail(email) {
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailPattern.test(email);
    }

    // Show error message for a specific input field
    function showError(input, message) {
        const error = document.createElement('span');
        error.className = 'error-message';
        error.textContent = message;
        input.classList.add('error');
        input.parentElement.appendChild(error);
    }

    // Clear all error messages
    function clearErrors() {
        const errors = document.querySelectorAll('.error-message');
        errors.forEach(error => error.remove());
        const inputs = document.querySelectorAll('.error');
        inputs.forEach(input => input.classList.remove('error'));
    }
});

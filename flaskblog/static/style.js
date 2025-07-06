document.addEventListener('DOMContentLoaded', function() {
    // Function to display flash messages
    function showFlashMessage(message, category) {
        const flashContainer = document.getElementById('flash-messages');
        const flashMessage = document.createElement('div');
        flashMessage.className = `flash-message ${category}`;
        
        const messageText = document.createElement('span');
        messageText.textContent = message;
        
        const closeButton = document.createElement('button');
        closeButton.className = 'flash-close';
        closeButton.innerHTML = '&times;';
        closeButton.addEventListener('click', function() {
            flashMessage.style.animation = 'slideOut 0.5s forwards';
            setTimeout(() => flashMessage.remove(), 500);
        });
        
        flashMessage.appendChild(messageText);
        flashMessage.appendChild(closeButton);
        flashContainer.appendChild(flashMessage);
        
        // Auto-remove after 5 seconds
        setTimeout(() => {
            flashMessage.style.animation = 'slideOut 0.5s forwards';
            setTimeout(() => flashMessage.remove(), 500);
        }, 5000);
    }

    // Check for Fla flashed messages
    const flaskFlashes = document.querySelectorAll('.flashes li');
    flaskFlashes.forEach(flash => {
        const message = flash.textContent;
        let category = 'info';
        
        if (flash.classList.contains('success')) category = 'success';
        if (flash.classList.contains('error')) category = 'error';
        if (flash.classList.contains('warning')) category = 'warning';
        
        showFlashMessage(message, category);
        flash.remove();
    });

    // Global function to show messages from other scripts
    window.showFlash = function(message, category = 'info') {
        showFlashMessage(message, category);
    };
});

// this is the code for the registration page
// Form input animations
document.querySelectorAll('.cyberpunk-input').forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.querySelector('.input-label').style.color = 'var(--primary)';
    });

    input.addEventListener('blur', function() {
        this.parentElement.querySelector('.input-label').style.color = 'var(--accent)';
    });
});

// Form validation styling
function styleFormErrors(form) {
    const inputs = form.querySelectorAll('input');
    inputs.forEach(input => {
        if (input.classList.contains('is-invalid')) {
            input.style.borderColor = 'var(--error)';
            input.style.boxShadow = '0 0 8px var(--error)';
        }
    });
}

// Apply styling when page loads
document.addEventListener('DOMContentLoaded', function() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        styleFormErrors(form);
    });
});

// this is for otp page
// OTP input animation
document.querySelectorAll('.cb-input-194826').forEach(input => {
    // Add terminal-style cursor effect
    input.addEventListener('focus', function() {
        this.style.borderBottom = '2px solid #c4b5fd';
        this.parentElement.querySelector('.cb-input-label-926485').style.color = '#8b5cf6';
    });

    input.addEventListener('blur', function() {
        this.style.borderBottom = '2px solid #8b5cf6';
        this.parentElement.querySelector('.cb-input-label-926485').style.color = '#c4b5fd';
    });

    // Simulate terminal input for OTP fields
    input.addEventListener('input', function() {
        this.style.letterSpacing = '0.5rem';
    });
});
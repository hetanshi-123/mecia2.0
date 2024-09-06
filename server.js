function handleFormSubmit(event) {
    event.preventDefault(); // Prevent the form from submitting normally

    // Hide the form and show the confirmation message
    document.getElementById('donation-form').style.display = 'none';
    document.getElementById('confirmation-message').style.display = 'block';
}
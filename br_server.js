document.getElementById('registrationForm').addEventListener('Register', function(event) {
    event.preventDefault();

    const Name = document.getElementById('Name').value;
    const Email = document.getElementById('Email').value;
    const Contact_no = document.getElementById('Contact No.').value;
    const Address = document.getElementById('Address').value;

    fetch('/Register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ Name, Email, Contact_no, Address }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').innerText = data.message;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});

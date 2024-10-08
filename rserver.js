document.getElementById('registrationForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name, email, password })
        });

        const result = await response.json();

        if (response.ok) {
            document.getElementById('message').textContent = 'Registration successful!';
        } else {
            document.getElementById('message').textContent = Error: ${result.message};
        }
    } catch (error) {
        document.getElementById('message').textContent = 'Error: Could not reach the server.';
    }
});
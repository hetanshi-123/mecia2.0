document.addEventListener('DOMContentLoaded', () => {
    const wasteCheckbox = document.getElementById('wasteCheckbox');
    const donationCheckbox = document.getElementById('donationCheckbox');
    const wasteOptions = document.getElementById('wasteOptions');
    const donationOptions = document.getElementById('donationOptions');

    wasteCheckbox.addEventListener('change', () => {
        wasteOptions.classList.toggle('hidden', !wasteCheckbox.checked);
    });

    donationCheckbox.addEventListener('change', () => {
        donationOptions.classList.toggle('hidden', !donationCheckbox.checked);
    });
});
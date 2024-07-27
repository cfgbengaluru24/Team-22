document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('areaForm');

    form.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        const formData = new FormData(form); // Create a FormData object from the form

        fetch('/api/save_data/', { // Update this URL to your API endpoint
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value // Include CSRF token for Django
            }
        })
        .then(response => response.json()) // Parse JSON response
        .then(data => {
            if (data.success) {
                alert('Data submitted successfully!');
                window.location.href = "{% url 'index' %}" // Optionally reset the form
            } else {
                alert('Error: ' + data.message);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('There was an error submitting the form.');
        });
    });
});

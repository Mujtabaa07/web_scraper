document.addEventListener('DOMContentLoaded', function() {
    const deleteForms = document.querySelectorAll('form[action^="/delete"]');
    
    deleteForms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const confirmed = confirm('Are you sure you want to delete this article?');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    });
});
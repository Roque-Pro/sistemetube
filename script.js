document.getElementById('downloadForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var formData = new FormData(this);

    fetch('/download', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('downloadStatus').textContent = data.message;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});

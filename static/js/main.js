function searchPhotos() {
    var searchTerm = document.getElementById("searchbar").value;
    $.get('/search?q=' + encodeURIComponent(searchTerm), function(data) {
        var imageGrid = $('#images');
        imageGrid.empty();
        data.forEach(function(imageUrl) {
            imageGrid.append('<img src="' + imageUrl + '" class="img-thumbnail">');
        });
    });
}

function toggleUploadHandler() {
    var handler = document.querySelector('.upload_photo_handler');
    handler.style.display = handler.style.display === 'none' ? 'block' : 'none';
}

function uploadPhotos() {
    var file = $('#file')[0].files[0];
    var labels = $('#labels').val();
    
    var formData = new FormData();
    formData.append('file', file);
    formData.append('custom_labels', labels);

    $.ajax({
        url: '/upload',
        type: 'PUT',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response) {
            alert('File uploaded successfully');
        },
        error: function(xhr, status, error) {
            alert('Error uploading file: ' + error);
        }
    });
}
function renderImages(urls) {
    var imageGrid = $('#images');
    imageGrid.empty();

    if (!urls || urls.length === 0) {
        imageGrid.append('<p class="empty-state">No matching photos found.</p>');
        return;
    }

    urls.forEach(function(imageUrl) {
        imageGrid.append('<img src="' + imageUrl + '" class="img-thumbnail">');
    });
}

function searchPhotos() {
    var searchTerm = document.getElementById("searchbar").value;
    $.get('/search?q=' + encodeURIComponent(searchTerm), function(data) {
        renderImages(data);
    });
}

function toggleUploadHandler() {
    var handler = document.querySelector('.upload_photo_handler');
    handler.classList.toggle('open');
}

function uploadPhotos() {
    var file = $('#file')[0].files[0];
    var labels = $('#labels').val();

    if (!file) {
        alert('Please choose a file first');
        return;
    }

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
            alert(response.message || 'File uploaded successfully');
            // Preview the picked file immediately since demo mode doesn't persist uploads.
            $('#images').prepend('<img src="' + URL.createObjectURL(file) + '" class="img-thumbnail">');
        },
        error: function(xhr, status, error) {
            var message = (xhr.responseJSON && xhr.responseJSON.error) || error || 'Unknown error';
            alert('Error uploading file: ' + message);
        }
    });
}

$(function() {
    searchPhotos();

    $('#searchbar').on('keypress', function(e) {
        if (e.which === 13) {
            searchPhotos();
        }
    });
});

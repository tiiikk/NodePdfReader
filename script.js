const dropZones = document.querySelectorAll('.file-input');
const submitButton = document.querySelector('button[type="submit"]');

// Prevent default behavior for dragover and dragenter events
dropZones.forEach(dropZone => {
    dropZone.addEventListener('dragover', e => {
        e.preventDefault();
    });

    dropZone.addEventListener('dragenter', e => {
        e.preventDefault();
    });
});

// Handle file drop event
dropZones.forEach(dropZone => {
    dropZone.addEventListener('drop', e => {
        e.preventDefault();
        const file = e.dataTransfer.files[0];
        const input = dropZone.querySelector('.file-input');
        input.files = e.dataTransfer.files;
        console.log(`File dropped: ${file.name}`);
    });
});


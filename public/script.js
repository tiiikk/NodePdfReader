const dropZones = document.querySelectorAll('.input-container');
const wait_text = document.querySelector('.waiting_text');
const submit_btn = document.getElementById('submit_btn');
const responseDiv = document.getElementById('response');


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
    });
});


// submit_btn.addEventListener('click', c =>{
//     wait_text.classList.remove('hidden')
// })

const firstFileInput = document.getElementById('first-file');
const secondFileInput = document.getElementById('second-file');
const warningDiv = document.getElementById('warning');

wait_text.classList.add('hidden')

// Uncomment the submit_btn event listener
submit_btn.addEventListener('click', async event => {
    event.preventDefault();

    if (!firstFileInput.value.trim() || !secondFileInput.value.trim()) {
        warningDiv.textContent = 'Both input containers must not be empty. Please select files.';
        warningDiv.classList.remove('hidden');
    } else {
        // Hide warning message and show "waiting" text
        responseDiv.classList.add('hidden');

        warningDiv.classList.add('hidden');
        wait_text.classList.remove('hidden');

        // Create a FormData object and append the selected files to it
        const formData = new FormData();
        formData.append('file1', firstFileInput.files[0]);
        formData.append('file2', secondFileInput.files[0]);

        try {
            // Send a POST request to the server
            const response = await fetch('/', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                const responseData = await response.text();
                console.log('Server Response:', responseData);
                // Display the server response in the "response" div
                responseDiv.innerHTML = `<p>${responseData}</p>`;
                if (responseData.includes('PASSED')) {
                    responseDiv.firstChild.style.color = 'greenyellow';
                } else if (responseData.includes('FAILED')) {
                    responseDiv.firstChild.style.color = 'red';
                }
                responseDiv.classList.remove('hidden');
                wait_text.classList.add('hidden');

            } else {
                console.error('Server Error:', response.statusText);
                // Handle error if needed
            }
        } catch (error) {
            console.error('Error:', error);
            // Handle fetch error if needed
        }
    }
});
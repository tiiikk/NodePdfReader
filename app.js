const express = require('express');
const multer = require('multer');
const path = require('path');

const { spawn } = require('child_process');
// const { readFile } = require('fs/promises');
// const { appendFile } = require('fs/promises');

const app = express();

// Define the storage configuration for multer
const storage = multer.diskStorage({
    destination: 'uploads/',
    filename: function(req, file, cb) {
        let filename;
        if (file.fieldname === 'file1') {
            filename = 'first.pdf';
        } else if (file.fieldname === 'file2') {
            filename = 'second.pdf';
         }// else if (file.fieldname === 'file3'){
        //     // Handle other cases or provide a default filename if needed
        //     filename = 'third.pdf';
        // }
        cb(null, filename);
    }
});

// Initialize multer with the storage configuration
const upload = multer({ storage });

// Serve static files
app.use(express.static(path.join(__dirname, 'public')));

// Route for the root URL
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));

});
// , {name: 'file3'}
// Route for handling form submission and file uploads
app.post('/',  upload.fields([{ name: 'file1' }, { name: 'file2' }]), async (req, res) => {
    const files = [];

    if (req.files['file1']) {
        const file1 = {
            originalname: req.files['file1'][0].originalname,
        };
        files.push(file1);
    }

    if (req.files['file2']) {
        const file2 = {
            originalname: req.files['file2'][0].originalname,
        };
        files.push(file2);
    }
    // if (req.files['file3']) {
    //     const file3 = {
    //         originalname: req.files['file3'][0].originalname,
    //         // filename: req.files['file2'][0].filename
    //     };
    //     files.push(file3);
    // }

    // Handle form submission and file uploads here
    res.send(`Form submitted and files uploaded successfully: ${JSON.stringify(files)}`);

    const childPy = spawn('python', ['all_in_one.py']);

    childPy.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
    });

    childPy.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
    });

    childPy.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
    });

});


app.listen(3001, () => {
    console.log('Server listening on port 3001');
});

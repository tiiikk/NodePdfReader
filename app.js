const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');

const { spawn } = require('child_process');

const uploadsFolder = path.join(__dirname, 'uploads');



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
    // res.send(`Form submitted and files uploaded successfully: ${JSON.stringify(files)}`);

    const childPy = spawn('python', ['all_in_one.py']);

    let stdoutData = '';
    let stderrData = '';
    childPy.stdout.on('data', (data) => {
        stdoutData += data;
        console.log(`stdout: ${data}`);
    });

    childPy.stderr.on('data', (data) => {
        stderrData += data;
        console.error(`stderr: ${data}`);
    });

    childPy.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        // Send the Python output and errors back to the client
        res.send(`The files you compared\`: ${JSON.stringify(files[0]['originalname'])} - ${JSON.stringify(files[1]['originalname'])} \n The comparision results: \n${stdoutData.trim()}`);
        //deleteing the files in uploads directory after sending response

        fs.readdir(uploadsFolder, (err, files) => {
            if (err) {
                console.error('Error reading directory:', err);
                return;
            }

            files.forEach(file => {
                const filePath = path.join(uploadsFolder, file);
                fs.unlink(filePath, err => {
                    if (err) {
                        console.error(`Error deleting file ${file}:`, err);
                    }
                });
            });
        });
    });



});

app.listen(process.env.PORT || 3000, function () {
    console.log("SERVER STARTED PORT: 3000");
});
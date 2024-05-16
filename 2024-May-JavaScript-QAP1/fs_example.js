// Import the fs module to interact with the file system
const fs = require('fs');

// Define the path to the file to be written and read
const filePath = './example.txt';

// Write the string 'Hello, filesystem!\n' to the file at filePath
fs.writeFile(filePath, 'Hello, filesystem! This is the one and only DAVE HUSK for my QAP Full Stack JavaScript\n', (err) => {
  // Check for and log any errors that occur during writing
  if (err) {
    return console.error(`Error writing file: ${err}`);
  }
  // Log a success message if the file is written successfully
  console.log('File written successfully');

  // Read the contents of the file
  fs.readFile(filePath, 'utf8', (err, data) => {
    // Check for and log any errors that occur during reading
    if (err) {
      return console.error(`Error reading file: ${err}`);
    }
    // Log the contents of the file
    console.log(`File contents: ${data}`);
  });
});

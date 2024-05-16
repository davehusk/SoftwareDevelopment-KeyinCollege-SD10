Dave Husk
May 16 2024
Full Stack JavaScript

## Questionaire

1. How long did it take?
   - I started at around 2pm after my last class was over, and it's now 2:43pm

2. What resources?
   - Used the transcripts to your classes and put them into an AI model to use RAG with it and ask/answer questions.
   - AI

3. Did I need help?
   - No

4. Did I need to ask questions? 
   - No

5. Rate difficulty
   - 1/2

## Step 1: Review All 11 Core Objects

1. **http**
   - Provides functionalities to create HTTP servers and clients.
   - Used to handle requests and responses in web applications.

2. **events**
   - Implements the EventEmitter class for handling events.
   - Essential for managing asynchronous operations.

3. **filesystem (fs)**
   - Offers functionalities to interact with the file system.
   - Used to read, write, and manipulate files and directories.

4. **console**
   - Provides a simple debugging console.
   - Commonly used for logging output to the terminal.

5. **buffer**
   - Deals with binary data directly in memory.
   - Useful for handling binary streams, such as reading files or network protocols.

6. **globals**
   - Includes globally accessible objects like `global`, `process`, `Buffer`, etc.
   - Provides access to essential runtime information and operations.

7. **stream**
   - Handles streaming data, such as file I/O and network communication.
   - Used to process large datasets or continuous data flow efficiently.

8. **url**
   - Provides utilities for URL resolution and parsing.
   - Useful for manipulating and resolving URL strings.

9. **path**
   - Offers utilities for working with file and directory paths.
   - Used to handle and transform file paths.

10. **os**
    - Provides operating system-related utility methods and properties.
    - Useful for retrieving system information, such as CPU, memory, and network interfaces.

11. **process**
    - Provides information about, and control over, the current Node.js process.
    - Used for handling process-related events and operations.

## Step 2: Choose Three Global Objects

I will select three of the most useful global objects for deep dives: **http**, **filesystem (fs)**, and **process**.

### 2.a. Descriptions

1. **http**
   - The `http` module in Node.js allows you to create HTTP servers and make HTTP requests. It is essential for building web applications and services. With `http`, you can listen to incoming requests on specific ports, handle routing, and serve responses to clients.

2. **filesystem (fs)**
   - The `fs` module provides an API for interacting with the file system in a manner closely modeled around standard POSIX functions. It can be used to read, write, delete, and manipulate files and directories. This module is crucial for tasks that involve file handling, such as reading configuration files, storing user uploads, or logging.

3. **process**
   - The `process` module provides information about the current Node.js process and allows you to interact with it. It includes properties and methods for handling the process's lifecycle, managing environment variables, and listening to process events. This module is vital for process management and configuration in Node.js applications.

## 2.b. Sample Code

Let's create sample files for each of the selected global objects.

1. **http_example.js**
   ```javascript
      // Import the http module to create an HTTP server
      const http = require('http');

      // Create an HTTP server that handles incoming requests
      const server = http.createServer((req, res) => {
      // Log the request method (e.g., GET, POST) and URL
      console.log(`Received request: ${req.method} ${req.url}`);

      // Set the response header to indicate a plain text response
      res.writeHead(200, { 'Content-Type': 'text/plain' });

      // Send a response message to the client
      res.end('Hello, World!\n');
      });

      // Make the server listen on port 3000 and log a message once it's ready
      server.listen(3000, () => {
      console.log('Server is listening on port 3000');
      });
   ```

2. **fs_example.js**
   ```javascript
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
   ```

3. **process_example.js**
   ```javascript
      // Log the current process ID
      console.log(`Process ID: ${process.pid}`);

      // Log the version of Node.js that is running
      console.log(`Node.js version: ${process.version}`);

      // Log the current working directory of the process
      console.log(`Current working directory: ${process.cwd()}`);

      // Log the process uptime in seconds
      console.log(`Process uptime: ${process.uptime()} seconds`);

      // Listen for the process exit event and log a message when it occurs
      process.on('exit', (code) => {
      console.log(`Process exiting with code: ${code}`);
      });

      // Simulate a process exit after 3 seconds
      setTimeout(() => {
      process.exit(0); // Exit the process with code 0 (success)
      }, 3000); // Wait for 3000 milliseconds (3 seconds)
   ```

## Step 3: Confirm Sample Code Execution

To confirm that all sample node files can be run without error using the terminal, navigate to the folder containing the files and type `node [solution file name]`. For example, to run the **http_example.js** file, type `node http_example.js`. The results written by the `console.log()` statements should be displayed in the terminal.

**http_example.js**
```
$ node http_example.js
Server is listening on port 3000
Received request: GET /
Received request: GET /favicon.ico
Received request: GET /favicon.ico
Received request: GET /
Received request: GET /favicon.ico
```
Open a web browser and navigate to `http://localhost:3000` to see the response "Hello, World!".

**fs_example.js**
```
$ node fs_example.js
File written successfully
File contents: Hello, filesystem! This is the one and only DAVE HUSK for my QAP Full Stack JavaScript
```
The file `example.txt` has been created in the current working directory with the specified contents.

**process_example.js**
```
$ node process_example.js
Process ID: 2892
Node.js version: v21.5.0
Current working directory: C:\Users\daveh\OneDrive\SoftwareDev\- KeyinCollege -\FullStack JS\QAP1 - FS JS
Process uptime: 0.0312363 seconds
Process exiting with code: 0
```
The process exits after 3 seconds, and the exit code is 0.

I successfully reviewed the 11 core global objects in Node.js, three objects for a deep dive, and sample code to demo their usage.
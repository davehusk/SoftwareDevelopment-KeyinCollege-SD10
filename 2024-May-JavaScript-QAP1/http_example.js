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

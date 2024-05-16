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

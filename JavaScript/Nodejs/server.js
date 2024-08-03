const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path'); // Import the path module

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve the static files from the 'public' directory
app.use(express.static(path.join(__dirname, 'public')));

let users = {};
let connectedUsersCount = 0; // Track the number of connected users

io.on('connection', (socket) => {
  socket.on('disconnect', () => {
    console.log('User disconnected');
    if (users[socket.id]) {
      io.emit('user left', { username: users[socket.id] });
      delete users[socket.id];
      connectedUsersCount--; // Decrease the count when a user disconnects
    }
  });

  socket.on('new user', (username) => {
    console.log('New user joined:', username);
    users[socket.id] = username;
    connectedUsersCount++; // Increase the count when a new user joins

    // Check if there are two users connected
    if (connectedUsersCount === 2) {
      // Emit an event to enable chatting
      io.emit('chat enabled');
    }
  });

  socket.on('chat message', (msg) => {
    io.emit('chat message', { username: users[socket.id], message: msg });
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

const API_URL = "http://localhost:8000";

let board, game = new Chess();

function login() {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  
  fetch(`${API_URL}/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password })
  })
  .then(res => res.json())
  .then(data => {
    if (data.token) {
      localStorage.setItem('token', data.token);
      document.getElementById('playerName').innerText = username;
      document.getElementById('loginSection').style.display = 'none';
      document.getElementById('gameSection').style.display = 'block';
      board = Chessboard('board', { draggable: true, position: 'start' });
    } else {
      alert('Login failed');
    }
  });
}

function startNewGame() {
  game.reset();
  board.position('start');
}

function saveMatchHistory(opponent, result, moves) {
    const token = localStorage.getItem('token');
    fetch(`${API_URL}/savegame`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        player: localStorage.getItem('username'),
        opponent: opponent,
        result: result,
        moves: moves
      })
    });
  }

function loadMatchHistory() {
    const username = localStorage.getItem('username');
    fetch(`${API_URL}/history/${username}`)
    .then(res => res.json())
    .then(games => {
    const historyDiv = document.getElementById('historySection');
    historyDiv.innerHTML = '<h2>Your Match History</h2>';
    games.forEach(g => {
        historyDiv.innerHTML += `<div>${g.date}: vs ${g.opponent} - ${g.result}</div>`;
    });
    });
}
  
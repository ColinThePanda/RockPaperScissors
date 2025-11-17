const rock_button = document.getElementById("rock-button");
const paper_button = document.getElementById("paper-button");
const scissors_button = document.getElementById("scissors-button");

const win_result = `
<h2 class="win-result">You Win!</h2>
<button class="play-again" onclick="play_again()">Play Again</button>
`;
const lose_result = `
<h2 class="lose-result">You Lose</h2>
<button class="play-again" onclick="play_again()">Play Again</button>
`;
const tie_result = `
<h2 class="tie-result">It is a tie</h2>
<button class="play-again" onclick="play_again()">Play Again</button>
`;

function handle_rock() {
  handle_click(0);
}
function handle_paper() {
  handle_click(1);
}
function handle_scissors() {
  handle_click(2);
}

function handle_click(player_choice) {
  let result_div = document.getElementsByClassName("result")[0];
  if (result_div.innerHTML !== "") {
    return;
  }
  let ai_choice = Math.floor(Math.random() * 3);
  let winner = (3 + player_choice - ai_choice) % 3;

  if (winner === 1) {
    result_div.innerHTML = win_result;
  } else if (winner === 2) {
    result_div.innerHTML = lose_result;
  } else {
    result_div.innerHTML = tie_result;
  }
}

function play_again() {
  let result_div = document.getElementsByClassName("result")[0];
  result_div.innerHTML = "";
}

rock_button.addEventListener("click", handle_rock);
paper_button.addEventListener("click", handle_paper);
scissors_button.addEventListener("click", handle_scissors);

const API_URL = "http://127.0.0.1:8000";

// const loadBtn = document.getElementById("loadPlayerss");
// loadBtn.addEventListener("click", loadPlayers);
const loadBtn = document.getElementById("loadPlayerss");
if (loadBtn) {
    loadBtn.addEventListener("click", loadPlayers);
}


function loadPlayers(){
    fetch(API_URL + '/players',{
    headers: authHeaders()
}).then(function(response){
        return response.json();
    }).then(function(players){
        var list = document.getElementById("playerslist");
        list.innerHTML="";
        for (var i =0 ;i<players.length;i++){
            var li = document.createElement("li");
            li.innerText = players[i].name + " | Runs :" +players[i].runs;
            list.appendChild(li);
        }

    });
}


// #data with player name 

const singleBtn = document.getElementById("CheckInfo");

if (singleBtn){singleBtn.addEventListener("click", loadSinglePlayer);}

function loadSinglePlayer(){

    // const player_name = document.getElementById("player_name").value.trim();

    const player_name = document.getElementById("search_player_name").value.trim();


    if (!player_name) {
        alert("Please enter player name");
        return;
    }

    fetch(API_URL + "/players/name/" + encodeURIComponent(player_name), {
    headers: authHeaders()
}).then(response => {
            if (!response.ok) {
                throw new Error("Player not found");
            }
            return response.json();
        })
        .then(player => {

            const list = document.getElementById("playerslist");
            list.innerHTML = "";

            const li = document.createElement("li");
            li.innerText =
                `${player.name} | Runs: ${player.runs} | Matches: ${player.matches}
                 | Avg: ${player.average} | Wickets: ${player.wickets}`;

            list.appendChild(li);
        })
        .catch(err => {
            alert(err.message);
        });
}


document.addEventListener("DOMContentLoaded", function () {

    const Update_btn = document.getElementById("Update_player");

    if (!Update_btn) {
        console.error("Update_player button not found");
        return;
    }

    Update_btn.addEventListener("click", update_player);

});

// update player using inputs 
// const Update_btn = document.getElementById("Update_player");
// Update_btn.addEventListener("click",update_player);
// const Update_btn = document.getElementById("Update_player");
// if (Update_btn) {
//     Update_btn.addEventListener("click", update_player);
// }


function update_player(){
    // const player_name = document.getElementById("player_name").value.trim();
    const player_name = document.getElementById("update_player_name").value.trim();


    const update_data ={
        country: document.getElementById("CountryName").value || null ,
        role : document.getElementById("Role").value || null,
        batting_style:document.getElementById("battingstyle").value || null,
        bowling_style:  document.getElementById("BowlingStyle").value || null,
        matches: document.getElementById("matches").value
    ? parseInt(document.getElementById("matches").value)
    : null,


        runs: document.getElementById("runs").value ? parseInt(document.getElementById("runs").value):null,
        average :  document.getElementById("avg").value ? parseFloat(document.getElementById("avg").value) : null,
        wickets :  document.getElementById("wickets").value ? parseInt(document.getElementById("wickets").value) : null,
        strike_rate : document.getElementById("strikerate").value ? parseFloat(document.getElementById("strikerate").value):null,
        economy : document.getElementById("economy").value ? parseFloat(document.getElementById("economy").value):null,
        best_score : document.getElementById("bestscore").value || null,
        is_active : document.getElementById("is_active").checked ,
        join_date : document.getElementById("joinDate").value || null
    
    }

    if(!player_name){
        alert("player  name is required");
        return;
    }

    fetch(`${API_URL}/players/name/${encodeURIComponent(player_name)}`, {
    method: "PUT",
    headers: authHeaders(),
    body: JSON.stringify(update_data)
    }).then(function(response){
    if (!response.ok){
        throw new Error("player not found")
    }
    return response.json();


    }).then(function(update_data){
    console.log(update_data);
    displayUpdatedPlayer(update_data);

})
}





// player delete
function deletePlayer() {
    const id = document.getElementById("player_id").value;

    fetch(`${API_URL}/players/${id}`, {
        method: "DELETE",
        headers: authHeaders()
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


// Post method









// Machine learning model 
function predictML() {
    const data = {
        matches: parseInt(document.getElementById("ml_matches").value),
        runs: parseInt(document.getElementById("ml_runs").value),
        average: parseFloat(document.getElementById("ml_avg").value),
        wickets: parseInt(document.getElementById("ml_wickets").value)
    };

    fetch(API_URL + "/ml/predict", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify(data)
    })
    .then(r=>r.json())
    .then(d=>{
        document.getElementById("result").innerText =
            "AI Prediction: " + d.ai_result;
    });
}






// login functionality
function login() {
    const data = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value
    };

    fetch(API_URL + "/auth/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => {
        if (!res.ok) throw new Error("Invalid login");
        return res.json();
    })
    .then(data => {
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("role", data.role);

        window.location.href = "index.html";
    })
    .catch(err => {
        document.getElementById("msg").innerText = err.message;
    });
}




// Auth Header
function authHeaders() {
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + localStorage.getItem("token")
    };
}



// Admin button Hide Logics
function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("role");
    window.location.href = "login.html";
}

document.addEventListener("DOMContentLoaded", () => {
    const role = localStorage.getItem("role");

    if (role !== "admin") {
        document.querySelectorAll(".admin-only")
            .forEach(el => el.style.display = "none");
    }
});




// Insert player 
function insertPlayer() {

    const data = {
        name: document.getElementById("name").value,
        country: document.getElementById("CountryName").value,
        role: document.getElementById("Role").value,
        batting_style: document.getElementById("battingstyle").value,
        bowling_style: document.getElementById("BowlingStyle").value,

        matches: document.getElementById("matches").value
            ? parseInt(document.getElementById("matches").value)
            : 0,

        runs: document.getElementById("runs").value
            ? parseInt(document.getElementById("runs").value)
            : 0,

        average: document.getElementById("avg").value
            ? parseFloat(document.getElementById("avg").value)
            : 0,

        wickets: document.getElementById("wickets").value
            ? parseInt(document.getElementById("wickets").value)
            : 0,

        strike_rate: document.getElementById("strikerate").value
            ? parseFloat(document.getElementById("strikerate").value)
            : 0,

        economy: document.getElementById("economy").value
            ? parseFloat(document.getElementById("economy").value)
            : 0,

        best_score: document.getElementById("bestscore").value,
        is_active: document.getElementById("is_active").checked,
        join_date: document.getElementById("joinDate").value
    };

    fetch(API_URL + "/players/insert", {
        method: "POST",
        headers: authHeaders(),
        body: JSON.stringify(data)
    })
    .then(res => {
        if (!res.ok) throw new Error("Insert failed");
        return res.json();
    })
    .then(player => {
        alert("Player inserted successfully");
        console.log(player);
        loadPlayers();
    })
    .catch(err => alert(err.message));
}








// Chat bot regarding 
function sendChat() {
    const msg = document.getElementById("chat_input").value;

    fetch(API_URL + "/chat/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("chat_reply").innerText = data.reply;
    })
    .catch(err => {
        document.getElementById("chat_reply").innerText = "Error";
    });
}



// registered regarding
function registerUser() {

    const data = {
        username: document.getElementById("reg_username").value.trim(),
        password: document.getElementById("reg_password").value.trim(),
        role: document.getElementById("reg_role").value
    };

    if (!data.username || !data.password) {
        document.getElementById("reg_msg").innerText = "All fields are required";
        return;
    }

    fetch(API_URL + "/auth/register", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => {
        if (!res.ok) throw new Error("Registration failed");
        return res.json();
    })
    .then(() => {
        alert("User registered successfully");
        window.location.href = "login.html";
    })
    .catch(err => {
        document.getElementById("reg_msg").innerText = err.message;
    });
}

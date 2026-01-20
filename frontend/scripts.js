const API_URL = "http://127.0.0.1:8000";

const loadBtn = document.getElementById("loadPlayerss");
loadBtn.addEventListener("click", loadPlayers);

function loadPlayers(){
    fetch(API_URL + '/players').then(function(response){
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

// const single_player = document.getElementById("Check Info");
// single_player.addEventListener("click",loadsingle);

// function loadsingle(){
//     fetch(API_URL +'/players/name/' + player_name).then(function(response){
//         return response.json();
//     }).then(function(players1){
//         var list1 = document.getElementById("player bio");
//         list1.innerHTML ="";
//     }).then()
// }



document.addEventListener("DOMContentLoaded", function () {

    const Update_btn = document.getElementById("Update_player");

    if (!Update_btn) {
        console.error("Update_player button not found");
        return;
    }

    Update_btn.addEventListener("click", update_player);

});

// update player using inputs 
const Update_btn = document.getElementById("Update_player");
Update_btn.addEventListener("click",update_player);

function update_player(){
    const player_name = document.getElementById("player_name").value.trim();

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
        join_date : document.getElementById("joinDate").value 

        }

fetch(`${API_URL}/players/name/${encodeURIComponent(player_name)}`, {
    method: "PUT",
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify(update_data)
})
.then(function(response){
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
        method: "DELETE"
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}


// Post method









// Machine learning model 
function predictML() {

    const data = {
        matches: parseInt(document.getElementById("matches").value),
        runs: parseInt(document.getElementById("runs").value),
        average: parseFloat(document.getElementById("average").value),
        wickets: parseInt(document.getElementById("wickets").value)
    };

    fetch("http://127.0.0.1:8000/ml/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(d => {
        document.getElementById("result").innerText =
            "AI Prediction: " + d.ai_result;
    });
}

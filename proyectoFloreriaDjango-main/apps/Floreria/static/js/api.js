function load(){
    api();
}
function api(){
    fetch('https://api.openweathermap.org/data/2.5/weather?q=Santiago,cl&appid=8e0fbec3b7c0b0c9ee3f7d777e666eac')
        .then(response => response.json())
        .then(data =>{  
            let clima = document.getElementById("apiClima");
            clima.innerHTML += (data.main.temp - 273.15).toFixed(1) + "°C";
        })
        console.log(clima);
}
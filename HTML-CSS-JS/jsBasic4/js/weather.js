const weather = document.querySelector(".js-weather");

const COORD = "coords";
const API_KEY = "d250855d28b52a4b5c215e1f535849fd";

function getWeather(lat, lon) {
    fetch(
        `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
    )
        .then(function(respons) {
            return respons.json();
        })
        .then(function(json) {
            const temp = json.main.temp;
            const place = json.name;
            weather.innerText = `${temp}℃ @ ${place}`;
        });
}

function saveCoords(coordObj) {
    localStorage.setItem(COORD, JSON.stringify(coordObj));
}

function handleGeoSucces(pos) {
    const latitude = pos.coords.latitude;
    const longitude = pos.coords.longitude;
    const coordsObj = {
        latitude,
        longitude
    };

    saveCoords(coordsObj);
    getWeather(latitude, longitude);
}

function handleGeoErr() {
    console.log("Can't access geo location");
}

function askForCoord() {
    navigator.geolocation.getCurrentPosition(handleGeoSucces, handleGeoErr);
}

function loadCoords() {
    const loadCoords = localStorage.getItem(COORD);
    if (loadCoords === null) {
        askForCoord();
    } else {
        const parse = JSON.parse(loadCoords);
        getWeather(parse.latitude, parse.longitude);
    }
}

function init() {
    loadCoords();
}

init();

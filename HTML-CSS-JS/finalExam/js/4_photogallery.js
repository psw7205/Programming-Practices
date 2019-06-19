function showing(elem) {
    document.getElementById("name").innerHTML = elem.alt;
    document.getElementById("image").style.backgroundImage = "url(" + elem.src + ")";
}

function original() {
    document.getElementById("image").style.backgroundImage = "url('')";
}
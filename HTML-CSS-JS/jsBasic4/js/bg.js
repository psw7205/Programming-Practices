const body = document.querySelector("body");

const NUM_IMG = 3;

function paintImg(imgNumber) {
  const img = new Image();
  img.src = `/imgs/${imgNumber}.jpg`;
  body.appendChild(img);
  img.classList.add("bgImg");
}

function genNum() {
  return Math.floor(Math.random() * NUM_IMG);
}

function init() {
  const randomNumber = genNum();
  paintImg(randomNumber);
}

init();

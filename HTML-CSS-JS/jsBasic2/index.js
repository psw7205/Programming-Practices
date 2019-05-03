// document의 함수로 객체 가져오기
const title = document.querySelector("#title");

const BASE_COLOR = "rgb(0, 255, 0)";
const OTHER_COLOR = "#ff0000";

function handleClick() {
  const currentColor = title.style.color;

  if (currentColor === BASE_COLOR) {
    title.style.color = OTHER_COLOR;
  } else {
    title.style.color = BASE_COLOR;
  }
}

function init() {
  title.style.color = BASE_COLOR;
  title.addEventListener("click", handleClick);
}

init();

function handleOffline() {
  console.log("byebye");
}

window.addEventListener("offline", handleOffline);

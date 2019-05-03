const form = document.querySelector(".js-form"),
  input = form.querySelector("input"),
  greeting = document.querySelector(".js-greeting");

const LOCAL_USER = "currentUser";
const CLASS_SHOWING = "showing";

function saveName(text) {
  localStorage.setItem(LOCAL_USER, text);
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = input.value;
  paintGreet(currentValue);
  saveName(currentValue);
}

function askForName() {
  form.classList.add(CLASS_SHOWING);
  form.addEventListener("submit", handleSubmit);
}

function paintGreet(text) {
  form.classList.remove(CLASS_SHOWING);
  greeting.classList.add(CLASS_SHOWING);
  greeting.innerText = `Hello ${text}`;
}

function loadName() {
  const currentUser = localStorage.getItem(LOCAL_USER);
  if (currentUser === null) {
    askForName();
  } else {
    paintGreet(currentUser);
  }
}

function init() {
  loadName();
}

init();

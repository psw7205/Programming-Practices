const todoForm = document.querySelector(".js-todo"),
  todoInput = todoForm.querySelector("input"),
  todoList = document.querySelector(".js-todoList");

const LOCAL_TODO = "todo";
let todoArray = [];

function saveTodo() {
  localStorage.setItem(LOCAL_TODO, JSON.stringify(todoArray));
}

function delTodo(event) {
  const li = event.target.parentNode;
  todoList.removeChild(li);
  const clean = todoArray.filter(function(todo) {
    return todo.id !== parseInt(li.id);
  });

  todoArray = clean;
  saveTodo();
}

function paintValue(text) {
  if (text === "") return;

  const li = document.createElement("li");
  const btn = document.createElement("button");
  const newId = todoArray.length;

  const obj = {
    text: text,
    id: newId
  };

  btn.addEventListener("click", delTodo);
  btn.innerHTML = "X";
  li.id = newId;
  li.innerText = text;
  li.append(btn);
  todoList.appendChild(li);

  todoArray.push(obj);
  saveTodo();
}

function handleSubmit(event) {
  event.preventDefault();
  const currentValue = todoInput.value;
  paintValue(currentValue);
  todoInput.value = "";
}

function loadTodos() {
  const loadedTodo = localStorage.getItem(LOCAL_TODO);
  if (loadedTodo !== null) {
    const parsed = JSON.parse(loadedTodo);
    parsed.forEach(function(todo) {
      paintValue(todo.text);
    });
  }
}

function init() {
  loadTodos();
  todoForm.addEventListener("submit", handleSubmit);
}

init();

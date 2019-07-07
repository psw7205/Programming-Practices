"use strict";
// 인터페이스를 이용한 클래스 구현
var Todo = /** @class */ (function() {
  function Todo(name, description, completed) {
    this.name = name;
    this.description = description;
    this.completed = completed;
  }
  return Todo;
})();
// Todo배열을 포함하는 TodoList클래스
var TodoList = /** @class */ (function() {
  function TodoList() {}
  //새 할 일 목록
  TodoList.prototype.createTodoItem = function(name, description) {
    var newItem = new Todo(name, description, false);
    var totalCount = TodoList.allTodos.push(newItem);
    return totalCount;
  };
  // Todo배열 리턴
  TodoList.prototype.allTodoItems = function() {
    return TodoList.allTodos;
  };
  TodoList.allTodos = new Array();
  return TodoList;
})();
window.onload = function() {
  var task = document.getElementById("todoName");
  var description = document.getElementById("todoDescription");
  // 버튼 클릭 시 이벤트 추가
  document.getElementById("add").addEventListener("click", function() {
    return toAlltask(task.value, description.value);
  });
};
// 버튼 클릭시 호출되는 함수
function toAlltask(task, description) {
  var todo = new TodoList();
  // 새 일정 추가
  todo.createTodoItem(task, description);
  // 일정 업데이트
  var div = document.getElementById("todoList");
  var list = "";
  for (var index = 0; index < TodoList.allTodos.length; index++) {
    list =
      list +
      TodoList.allTodos[index].name +
      " : " +
      TodoList.allTodos[index].description +
      "</br>";
  }
  div.innerHTML = list;
  //Casting
  document.getElementById("todoName").value = "";
  document.getElementById("todoDescription").value = "";
}
//# sourceMappingURL=todo.js.map

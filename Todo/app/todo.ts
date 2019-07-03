// 인터페이스 정의 -> 실제 자바스크립트로는 변환 X
interface ITodo {
    name: string;
    description: string;
    completed: boolean;
}

// 인터페이스를 이용한 클래스 구현
class Todo implements ITodo {
    constructor(public name: string, public description: string, public completed: boolean) { }

}

// Todo배열을 포함하는 TodoList클래스
class TodoList {
    public static allTodos: Todo[] = new Array;

    //새 할 일 목록
    createTodoItem(name: string, description: string): number {
        let newItem = new Todo(name, description, false);
        let totalCount: number = TodoList.allTodos.push(newItem);
        return totalCount;
    }

    // Todo배열 리턴
    allTodoItems(): Todo[] {
        return TodoList.allTodos;
    }
}

window.onload = function () {

    let task = <HTMLInputElement>document.getElementById("todoName");
    let description = <HTMLInputElement>document.getElementById("todoDescription");

    // 버튼 클릭 시 이벤트 추가
    document.getElementById("add").addEventListener('click', () => toAlltask(task.value, description.value));
}

// 버튼 클릭시 호출되는 함수
function toAlltask(task: string, description: string) {

    let todo = new TodoList();
    // 새 일정 추가
    todo.createTodoItem(task, description);

    // 일정 업데이트
    let div = <HTMLDivElement>document.getElementById("todoList");
    let list = "";

    for (let index = 0; index < TodoList.allTodos.length; index++) {
        list = list + TodoList.allTodos[index].name + " : " + TodoList.allTodos[index].description + '</br>';
    }
    div.innerHTML = list;

    //Casting
    (<HTMLInputElement>document.getElementById("todoName")).value = "";

    (<HTMLInputElement>document.getElementById("todoDescription")).value = "";

}
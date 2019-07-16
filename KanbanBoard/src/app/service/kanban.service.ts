import { Injectable } from '@angular/core';
import { Board } from '../model/board';
import { HttpClientModule } from '@angular/common/http';
import { Task } from '../model/task';
import { SubTask } from '../model/subtask';

@Injectable({
  providedIn: 'root'
})
export class KanbanService {
  public boards: Board[] = [];

  constructor(private http: HttpClientModule) {}

  public seedData(): Board {
    const tempTask: Task = new Task();
    const tempSubTask: SubTask = new SubTask();
    const board: Board = new Board();
    tempTask.id = 1;
    tempTask.title = 'Hello Task!!';
    tempTask.taskheaderID = '1';

    tempSubTask.id = '1';
    tempSubTask.title = 'Hello Task Header!!';

    tempTask.subtasks = [];
    tempTask.subtasks.push(tempSubTask);

    board.id = '1';
    board.title = 'Hello Seed Board';
    board.task = [];
    board.task.push(tempTask);

    this.boards = [];
    this.boards.push(board);

    return board;
  }
}

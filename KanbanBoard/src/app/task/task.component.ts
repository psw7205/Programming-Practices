import {
  Component,
  Input,
  Output,
  OnInit,
  EventEmitter,
  ElementRef
} from '@angular/core';
import { ActivatedRoute } from '@angular/router';

import { KanbanService } from '../service/kanban.service';
import { Task } from '../model/task';
import { SubTask } from '../model/subtask';
import { Board } from '../model/board';

@Component({
  selector: 'app-task',
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css']
})
export class TaskComponent implements OnInit {
  @Input()
  task: Task;

  @Input()
  subTasks: SubTask[];

  @Output()
  public onAddsubTask: EventEmitter<SubTask>;

  boards: Board[];
  board: Board = new Board();
  editingtask = false;
  addsubTaskText: string;
  currentTitle: string;
  constructor(
    private el: ElementRef,
    private route: ActivatedRoute,
    private kanbanService: KanbanService
  ) {
    this.onAddsubTask = new EventEmitter();
  }

  ngOnInit() {
    const boardId = this.route.snapshot.params.id;
    if (boardId !== undefined) {
      this.boards = this.kanbanService.boards;
      console.log(this.boards);
      for (const v of this.boards) {
        if (v.id === boardId) {
          this.board = v;
          break;
        }
      }
    }
  }

  addtaskOnEnter(event: KeyboardEvent) {
    if (event.keyCode === 13) {
      this.updatetask();
    } else if (event.keyCode === 27) {
      this.cleadAddtask();
    }
  }

  addsubTask() {
    this.subTasks = this.subTasks || [];
    const newsubTask = {
      title: this.addsubTaskText
    } as SubTask;
    let selectedtask: Task;
    for (const v of this.board.task) {
      if (v.id === this.task.id) {
        selectedtask = v;
        break;
      }
    }

    if (selectedtask.subtasks === undefined) {
      selectedtask.subtasks = new Array();
    }
    selectedtask.subtasks.push(newsubTask);
    this.subTasks = selectedtask.subtasks;
    this.onAddsubTask.emit(newsubTask);
  }

  addsubTaskOnEnter(event: KeyboardEvent) {
    if (event.keyCode === 13) {
      if (this.addsubTaskText && this.addsubTaskText.trim() !== '') {
        this.addsubTask();
        this.addsubTaskText = '';
      } else {
        this.clearAddsubTask();
      }
    } else if (event.keyCode === 27) {
      this.clearAddsubTask();
    }
  }
  updatetask() {
    if (this.task.title && this.task.title.trim() !== '') {
      this.editingtask = false;
    } else {
      this.cleadAddtask();
    }
  }

  cleadAddtask() {
    this.task.title = this.currentTitle;
    this.editingtask = false;
  }

  edittask() {
    this.currentTitle = this.task.title;
    this.editingtask = true;
    const input = this.el.nativeElement
      .getElementsByClassName('task-header')[0]
      .getElementsByTagName('input')[0];

    setTimeout(() => {
      input.focus();
    }, 0);
  }

  enableAddsubTask() {
    const input = this.el.nativeElement
      .getElementsByClassName('add-subTask')[0]
      .getElementsByTagName('input')[0];

    setTimeout(() => {
      input.focus();
    }, 0);
  }

  updatetaskOnBlur() {
    if (this.editingtask) {
      this.updatetask();
      this.clearAddsubTask();
    }
  }

  addsubTaskOnBlur() {
    if (this.addsubTaskText && this.addsubTaskText.trim() !== '') {
      this.addsubTask();
    }
    this.clearAddsubTask();
  }

  clearAddsubTask() {
    this.addsubTaskText = '';
  }
}

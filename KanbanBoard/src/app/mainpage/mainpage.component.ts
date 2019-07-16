import { Component, OnInit } from '@angular/core';
import { Board } from '../model/board';
import { KanbanService } from '../service/kanban.service';

@Component({
  selector: 'app-mainpage',
  templateUrl: './mainpage.component.html',
  styleUrls: ['./mainpage.component.css']
})
export class MainpageComponent implements OnInit {
  boards: Board[] = [];
  constructor(private kanbanService: KanbanService) {}

  ngOnInit() {
    this.boards.push(this.kanbanService.seedData());
  }

  public addBoard() {
    const newBoard: Board = new Board();
    newBoard.id = this.boards.length + 1 + '';
    newBoard.task = Array();
    newBoard.title = 'New Board';
    this.boards.push(newBoard);
  }
}

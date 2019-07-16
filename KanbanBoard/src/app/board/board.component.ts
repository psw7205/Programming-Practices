import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { KanbanService } from '../service/kanban.service';
import { Board } from '../model/board';

@Component({
  selector: 'app-board',
  templateUrl: './board.component.html',
  styleUrls: ['./board.component.css']
})
export class BoardComponent implements OnInit {
  board: Board;
  constructor(
    private route: ActivatedRoute,
    private kanbanService: KanbanService,
    private location: Location
  ) {}

  ngOnInit() {
    const boardID = this.route.snapshot.paramMap.get('id');
    this.board = this.kanbanService.boards.find(board => board.id === boardID);
  }
}

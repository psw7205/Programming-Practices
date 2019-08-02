import { Component, OnInit } from '@angular/core';
import { MessageService } from '../service/message.service';

@Component({
  selector: 'app-message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.css']
})
export class MessageComponent implements OnInit {
  // Angular에서는 public 으로 선언된 컴포넌트 프로퍼티만 바인딩 가능
  constructor(public ms: MessageService) {}

  ngOnInit() {}
}

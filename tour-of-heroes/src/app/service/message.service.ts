import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class MessageService {
  messages: string[] = [];
  constructor() {}

  push(text: string) {
    this.messages.push(text);
  }

  clear() {
    this.messages = [];
  }
}

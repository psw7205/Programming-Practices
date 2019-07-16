import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainpageComponent } from './mainpage/mainpage.component';
import { KanbanService } from './service/kanban.service';
import { BoardComponent } from './board/board.component';
import { TaskComponent } from './task/task.component';
import { SubtaskComponent } from './subtask/subtask.component';

@NgModule({
  declarations: [
    AppComponent,
    MainpageComponent,
    BoardComponent,
    TaskComponent,
    SubtaskComponent
  ],
  imports: [BrowserModule, AppRoutingModule, HttpClientModule, FormsModule],
  providers: [KanbanService],
  bootstrap: [AppComponent]
})
export class AppModule {}

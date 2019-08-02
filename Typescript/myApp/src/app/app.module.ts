import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { newsroutingmodule } from './app.route';
import { AppComponent } from './app.component';
import { NewsComponent } from './dashboard/news/news.component';
import { HeaderComponent } from './core/header/header.component';
import { FooterComponent } from './core/footer/footer.component';
import { NewsAPIService } from './service/newsapi.service';

@NgModule({
  declarations: [AppComponent, NewsComponent, HeaderComponent, FooterComponent],
  imports: [BrowserModule, newsroutingmodule, HttpClientModule],
  providers: [NewsAPIService],
  bootstrap: [AppComponent]
})
export class AppModule {}

import { Component, OnInit } from '@angular/core';
import { Article } from '../../../models/article';
import { News } from '../../../models/news';
import { IArticle } from '../../../models/IArticle';
import { catchError, map, tap } from 'rxjs/operators';
import { NewsAPIService } from '../../service/newsapi.service';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {
  type = 'business';
  news: News = new News(this.type);
  constructor(private service: NewsAPIService) {}
  ngOnInit() {
    this.service
      .fecthMyNews(this.type)
      .subscribe((items: News) => (this.news = items));
  }
}

import { Component, OnInit } from '@angular/core';
import { News } from '../../../models/news';
import { NewsAPIService } from '../../service/newsapi.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-news',
  templateUrl: './news.component.html',
  styleUrls: ['./news.component.css']
})
export class NewsComponent implements OnInit {
  type = 'health';
  news: News = new News(this.type);
  constructor(private service: NewsAPIService, private route: ActivatedRoute) {}
  ngOnInit() {
    this.route.data.subscribe(data => (this.type = data.type));
    this.service
      .fecthMyNews(this.type)
      .subscribe((items: News) => (this.news = items));
  }
}

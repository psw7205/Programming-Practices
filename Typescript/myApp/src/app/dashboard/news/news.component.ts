import { Component, OnInit } from "@angular/core";
import { Article } from "../../../models/article";
import { News } from "../../../models/news";

@Component({
  selector: "app-news",
  templateUrl: "./news.component.html",
  styleUrls: ["./news.component.css"]
})
export class NewsComponent implements OnInit {
  tmp: News = new News();

  private createArticleData(): Article[] {
    const articles: Article[] = new Array();
    articles.push({
      author: "박상우",
      title: "Sample News",
      desc: "Angular 연습 뉴스 컴포넌트",
      url: "http://naver.com",
      urlToImg: "",
      date: "2019-07-06"
    });

    articles.push({
      author: "박상우",
      title: "Sample News",
      desc: "Angular 연습 뉴스 컴포넌트",
      url: "http://naver.com",
      urlToImg: "",
      date: "2019-07-06"
    });

    return articles;
  }

  private createNewsData(): News {
    const news: News = new News();
    news.status = "ok";
    news.source = "PSW";
    news.sortBy = "top";
    news.articles = this.createArticleData();
    return news;
  }

  constructor() {}

  ngOnInit() {
    this.tmp = this.createNewsData();
  }
}

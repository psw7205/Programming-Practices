import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { HttpHeaders } from '@angular/common/http';
import { IArticle } from '../../models/IArticle';
import { Observable } from 'rxjs';

import { News } from '../../models/news';

import API_KEY from './API.json';

@Injectable()
export class NewsAPIService {
  constructor(private http: HttpClient) {
    this.base = 'https://newsapi.org/v2/top-headlines?country=kr&category=';
  }

  base: string;
  public fecthMyNews(category: string): Observable<News> {
    return this.http.get<News>(
      `${this.base}${category}&apiKey=${API_KEY.NewsAPIKey}&pagesize=10`
    );
  }
}

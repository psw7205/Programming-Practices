import { Article } from './article';
import { IArticle } from './IArticle';

export class News {
  private articles: IArticle[];
  constructor(public source: string) {}
}

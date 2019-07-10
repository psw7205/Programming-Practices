import { Article } from './article';

export class News {
  private articles: Article[];
  constructor(public source: string) {}
}

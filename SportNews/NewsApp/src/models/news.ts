import { Article } from './article';

export class News {
  public status: string;
  public source: string;
  public sortBy: string;
  public articles: Article[];
}

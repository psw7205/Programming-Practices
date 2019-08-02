import { IArticle } from './IArticle';

export class Article implements IArticle {
  public author: string;
  public title: string;
  public description: string;
  public url: string;
  public urlToImage: string;
  public publishedAt: string;
}

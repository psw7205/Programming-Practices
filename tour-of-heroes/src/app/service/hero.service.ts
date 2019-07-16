import { Injectable } from '@angular/core';
import { Hero } from '../../models/hero';
import { LIST } from '../../models/heroeslist';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root'
})
export class HeroService {
  getHeroList(): Observable<Hero[]> {
    this.ms.push('HeroService: fetched heroes');
    return of(LIST);
  }

  getHero(id: number): Observable<Hero> {
    this.ms.push(`HeroService: fetched hero=${id}`);
    return of(LIST.find(hero => hero.id === id));
  }

  constructor(private ms: MessageService) {}
}

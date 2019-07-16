import { Component, OnInit } from '@angular/core';
import { Hero } from '../../models/hero';
import { HeroService } from '../service/hero.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {
  heroes: Hero[];

  getHeroes(): void {
    this.hs.getHeroList().subscribe(list => (this.heroes = list));
    // this.heroes = this.hs.getHeroList();
  }

  constructor(private hs: HeroService) {}
  ngOnInit() {
    this.getHeroes();
  }
}

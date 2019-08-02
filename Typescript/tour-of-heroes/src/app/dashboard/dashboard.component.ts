import { Component, OnInit } from '@angular/core';

import { Hero } from '../../models/hero';
import { HeroService } from '../service/hero.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent implements OnInit {
  heroes: Hero[] = [];
  constructor(private hs: HeroService) {}

  ngOnInit() {
    this.getHeroes();
  }

  getHeroes(): void {
    this.hs
      .getHeroList()
      .subscribe(heroes => (this.heroes = heroes.slice(0, 8)));
  }
}

import { RouterModule, Routes } from '@angular/router';
import { ModuleWithProviders } from '@angular/core';

import { NewsComponent } from './dashboard/news/news.component';

const routes: Routes = [
  { path: '', redirectTo: 'business', pathMatch: 'full' },
  {
    path: 'business',
    component: NewsComponent,
    data: { type: 'business' }
  },
  {
    path: 'health',
    component: NewsComponent,
    data: { type: 'health' }
  },
  {
    path: 'science',
    component: NewsComponent,
    data: { type: 'science' }
  },
  {
    path: 'sports',
    component: NewsComponent,
    data: { type: 'sport' }
  },
  {
    path: '**',
    redirectTo: 'business',
    pathMatch: 'full'
  }
];

export const newsroutingmodule: ModuleWithProviders = RouterModule.forRoot(
  routes
);

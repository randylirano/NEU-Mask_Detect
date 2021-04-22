import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StoryComponent } from './story/story.component';
import { AboutComponent } from './about/about.component';
import { ProductComponent } from './product/product.component';
import { ConnectComponent } from './connect/connect.component';


const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: StoryComponent },
  { path: 'story', component: AboutComponent },
  { path: 'product', component: ProductComponent },
  { path: 'connect', component: ConnectComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { StoryComponent } from './story/story.component';
import { AboutComponent } from './about/about.component';
import { ProductComponent } from './product/product.component';
import { ConnectComponent } from './connect/connect.component';
import { VideoCaptureComponentComponent } from './video-capture-component/video-capture-component.component';
import { UploadImageComponentComponent } from './upload-image-component/upload-image-component.component';


const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'story', component: StoryComponent },
  { path: 'product', component: ProductComponent,
  children: [
    {path: 'image', component: UploadImageComponentComponent},
    {path: 'video', component: VideoCaptureComponentComponent},
  ]},
  { path: 'connect', component: ConnectComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HomeComponent } from './home/home.component';
import { StoryComponent } from './story/story.component';
import { AboutComponent } from './about/about.component';
import { ProductComponent } from './product/product.component';
import { ConnectComponent } from './connect/connect.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { HttpClientModule } from '@angular/common/http';
import { VideoCaptureComponentComponent } from './video-capture-component/video-capture-component.component';
import { UploadImageComponentComponent } from './upload-image-component/upload-image-component.component';



@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    StoryComponent,
    AboutComponent,
    ProductComponent,
    ConnectComponent,
    VideoCaptureComponentComponent,
    UploadImageComponentComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    NgbModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

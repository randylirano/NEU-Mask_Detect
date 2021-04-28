import { Component, OnInit, OnDestroy, ViewEncapsulation, Inject } from '@angular/core';
import { NgbCarouselConfig } from '@ng-bootstrap/ng-bootstrap';
import {DOCUMENT} from '@angular/common';



@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css'],
  encapsulation: ViewEncapsulation.None,
  providers: [NgbCarouselConfig]
})
export class HomeComponent implements OnInit, OnDestroy {
  images = [700, 800, 807].map((n) => `https://picsum.photos/id/${n}/900/500`);

  constructor( @Inject(DOCUMENT) private _document ) { }

  ngOnInit() {
    this._document.body.classList.add('bodybg-color');
  }

  ngOnDestroy() {
  // remove the class form body tag
  this._document.body.classList.remove('bodybg-color');
}

}

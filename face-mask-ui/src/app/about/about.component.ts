import { Component, OnInit, OnDestroy, ViewEncapsulation, Inject } from '@angular/core';
import {DOCUMENT} from '@angular/common';

@Component({
  selector: 'app-about',
  templateUrl: './about.component.html',
  styleUrls: ['./about.component.css'],
  encapsulation: ViewEncapsulation.None,

})
export class AboutComponent implements OnInit, OnDestroy {

  constructor( @Inject(DOCUMENT) private _document ) { }

  ngOnInit() {
    this._document.body.classList.add('aboutbody-color');
  }

  ngOnDestroy() {
  // remove the class form body tag
  this._document.body.classList.remove('aboutbody-color');
}

}

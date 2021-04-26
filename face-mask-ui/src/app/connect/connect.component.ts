import { Component, OnInit, OnDestroy, ViewEncapsulation, Inject  } from '@angular/core';
import {DOCUMENT} from '@angular/common';

@Component({
  selector: 'app-connect',
  templateUrl: './connect.component.html',
  styleUrls: ['./connect.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class ConnectComponent implements OnInit, OnDestroy {

  constructor( @Inject(DOCUMENT) private _document ) { }

  ngOnInit() {
    this._document.body.classList.add('connectbody-color');
  }

  ngOnDestroy() {
  // remove the class form body tag
  this._document.body.classList.remove('connectbody-color');
}

}

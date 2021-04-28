import { Component, OnInit, OnDestroy, ViewEncapsulation, Inject  } from '@angular/core';
import {DOCUMENT} from '@angular/common';

@Component({
  selector: 'app-story',
  templateUrl: './story.component.html',
  styleUrls: ['./story.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class StoryComponent implements OnInit, OnDestroy  {

  constructor( @Inject(DOCUMENT) private _document ) { }

  ngOnInit() {
    this._document.body.classList.add('teambody-color');
  }

  ngOnDestroy() {
  // remove the class form body tag
  this._document.body.classList.remove('teambody-color');
}

}

import { Component, OnInit, OnDestroy, ViewEncapsulation, Inject } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {DOCUMENT} from '@angular/common';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css'],
  encapsulation: ViewEncapsulation.None,
})
export class ProductComponent implements OnInit, OnDestroy {
  fileData: File = null;
  previewUrl:any = null;

  constructor( private http: HttpClient, @Inject(DOCUMENT) private _document ) { }

  ngOnInit() {
    this._document.body.classList.add('productbody-color');
  }

  ngOnDestroy() {
  // remove the class form body tag
  this._document.body.classList.remove('productbody-color');
}

  onFileSelected(fileInput: any) {
    this.fileData = <File>fileInput.target.files[0];
    this.preview();
  }

  preview() {
    // Show preview
    const mimeType = this.fileData.type;
    if (mimeType.match(/image\/*/) == null) {
      return;
    }

    const reader = new FileReader();
    reader.readAsDataURL(this.fileData);
    reader.onload = (_event) => {
      this.previewUrl = reader.result;
    }
  }

  onFileUploaded() {
    const formData = new FormData();
    formData.append('file', this.fileData);
    this.http.post('', formData)
      .subscribe(res => {
        console.log(res);
        alert('SUCCESS !!');
      })
  }
}

import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.css']
})
export class ProductComponent implements OnInit {
  fileData: File = null;
  previewUrl:any = null;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
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

import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Component({
  selector: 'app-upload-image-component',
  templateUrl: './upload-image-component.component.html',
  styleUrls: ['./upload-image-component.component.css']
})
export class UploadImageComponentComponent implements OnInit {
  fileData: File = null;
  previewUrl:any = null;
  result: string;
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }onFileSelected(fileInput: any) {
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
    this.http.post('http://localhost:5000/uploader', formData)
      .subscribe(res => {
        console.log(res);
        alert('SUCCESS !!');
        this.result = res["status"]
      })
  }
}

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { UploadImageComponentComponent } from './upload-image-component.component';

describe('UploadImageComponentComponent', () => {
  let component: UploadImageComponentComponent;
  let fixture: ComponentFixture<UploadImageComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ UploadImageComponentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(UploadImageComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

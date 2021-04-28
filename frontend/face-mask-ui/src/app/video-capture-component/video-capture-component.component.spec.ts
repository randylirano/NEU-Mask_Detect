import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VideoCaptureComponentComponent } from './video-capture-component.component';

describe('VideoCaptureComponentComponent', () => {
  let component: VideoCaptureComponentComponent;
  let fixture: ComponentFixture<VideoCaptureComponentComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VideoCaptureComponentComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VideoCaptureComponentComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GetShortUrlComponent } from './get-short-url.component';

describe('GetShortUrlComponent', () => {
  let component: GetShortUrlComponent;
  let fixture: ComponentFixture<GetShortUrlComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ GetShortUrlComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(GetShortUrlComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

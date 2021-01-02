import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateShortUrlComponent } from './create-short-url.component';

describe('CreateShortUrlComponent', () => {
  let component: CreateShortUrlComponent;
  let fixture: ComponentFixture<CreateShortUrlComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreateShortUrlComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateShortUrlComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

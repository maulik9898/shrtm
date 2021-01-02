import { TestBed } from '@angular/core/testing';

import { ShorturlService } from './shorturl.service';

describe('ShorturlService', () => {
  let service: ShorturlService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ShorturlService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

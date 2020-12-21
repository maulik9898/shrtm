import { Component } from '@angular/core';
import {ShorturlService} from './shorturl.service';
import {Observable, Subscription} from 'rxjs';
import {ShortUrl} from './short-url';
import {ActivatedRoute, Routes} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';
  shortUrlSubs: Subscription;
  shortUrl: ShortUrl;


  constructor(private shortUrlApi: ShorturlService, private route: ActivatedRoute) {
  }

  getShortUrl(slug: string): void{
    this.shortUrlSubs = this.shortUrlApi.getShortUrl(slug).subscribe(res => {
      this.shortUrl = res;
    },
      console.error
    );
    }
  }



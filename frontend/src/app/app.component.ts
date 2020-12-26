import {Component, OnInit} from '@angular/core';
import {ShorturlService} from './service/shorturl.service';
import {Observable, Subscription} from 'rxjs';
import {ShortUrl} from './_model/short-url';
import {ActivatedRoute, Routes} from '@angular/router';
import {AuthService} from "./service/auth.service";



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  shortUrlSubs: Subscription;
  shortUrl: ShortUrl;




  constructor(
    private shortUrlApi: ShorturlService,
    private route: ActivatedRoute,
    public authService: AuthService
   ) {
  }

  getShortUrl(slug: string): void{
    this.shortUrlSubs = this.shortUrlApi.getShortUrl(slug).subscribe(res => {
      this.shortUrl = res;
    },
      console.error
    );
    }


  ngOnInit(): void {


  }
  }



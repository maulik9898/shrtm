import {Component, OnInit} from '@angular/core';
import {ShorturlService} from './service/shorturl.service';
import {Observable, Subscription} from 'rxjs';
import {ShortUrl} from './_model/short-url';
import {ActivatedRoute, Routes} from '@angular/router';
import {AuthService} from './service/auth.service';



@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';




  constructor(

   ) {
  }


  ngOnInit(): void {


  }
  }



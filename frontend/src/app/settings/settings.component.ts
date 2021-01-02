import { Component, OnInit } from '@angular/core';
import {AuthService} from '../service/auth.service';
import {ShorturlService} from '../service/shorturl.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.css']
})
export class SettingsComponent implements OnInit {
  apiKey: any;

  constructor(
    public authService: AuthService,
    public shortUrlService: ShorturlService
  ) {

  }


  ngOnInit(): void {
    this.shortUrlService.getUser().subscribe(res => {
      this.apiKey = res.apiKey;
    });
  }

  updateApiKey(): void{
    this.shortUrlService.updateApiKey().subscribe(res => {
      this.apiKey = res.apiKey;
    });
  }

}

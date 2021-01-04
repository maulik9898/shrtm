import { Component, OnInit } from '@angular/core';
import {ShorturlService} from '../service/shorturl.service';
import {ActivatedRoute} from '@angular/router';
import {AuthService} from '../service/auth.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  isNavbarCollapsed: any = true;

  constructor(
    private shortUrlApi: ShorturlService,
    private route: ActivatedRoute,
    public authService: AuthService
  ) { }

  ngOnInit(): void {
  }

}

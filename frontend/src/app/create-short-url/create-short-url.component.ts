import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {ShorturlService} from '../service/shorturl.service';
import {ShortUrl} from '../_model/short-url';

@Component({
  selector: 'app-create-short-url',
  templateUrl: './create-short-url.component.html',
  styleUrls: ['./create-short-url.component.css']
})
export class CreateShortUrlComponent implements OnInit {
 createLinkForm = new FormGroup({
    url: new FormControl(''),
    slug: new FormControl(''),
  });
  private data: ShortUrl;
  error: any;

  constructor(private shortUrlApi: ShorturlService) { }

  ngOnInit(): void {
  }
  createLink(): void{
    this.data = new ShortUrl(this.createLinkForm.controls.url.value, this.createLinkForm.controls.slug.value);

    this.shortUrlApi
      .createShortUrl(this.data).subscribe(res => {
        console.log(res);
        this.createLinkForm.reset(); },
      err => {
        console.log(err);
        this.error = err.error.error;
      });

  }

}

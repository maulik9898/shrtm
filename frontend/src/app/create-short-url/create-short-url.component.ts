import { Component, OnInit } from '@angular/core';
import {FormControl, FormGroup} from '@angular/forms';
import {ShorturlService} from '../service/shorturl.service';
import {ShortUrl} from '../_model/short-url';
import {faCopy, faEye, faEyeSlash} from '@fortawesome/free-regular-svg-icons';
import {faLink} from '@fortawesome/free-solid-svg-icons';
import { FormBuilder } from '@angular/forms';
import {Clipboard} from "@angular/cdk/clipboard";


@Component({
  selector: 'app-create-short-url',
  templateUrl: './create-short-url.component.html',
  styleUrls: ['./create-short-url.component.css']
})
export class CreateShortUrlComponent implements OnInit {

 createLinkForm = this.fb.group({
   url: [''],
   slug: [''],
   password: ['']
 });
  linkIcon = faLink;
  type = 'password';
  passwordVisibility = faEyeSlash;
  private data: ShortUrl;
  error: any;
  shortUrl = '';
  success = false;
  isInvalid = false;
  copyIcon = faCopy;

  constructor(private shortUrlApi: ShorturlService,
              private fb: FormBuilder,
              private clipboard: Clipboard) { }

  ngOnInit(): void {
  }
  createLink(): void{
    this.data = new ShortUrl(this.createLinkForm.controls.url.value);
    if (this.createLinkForm.controls.slug.value !== '' ){
      this.data.slug = this.createLinkForm.controls.slug.value;
    }
    if (this.createLinkForm.controls.password.value !== '' ){
      this.data.password = this.createLinkForm.controls.password.value;
    }

    this.shortUrlApi
      .createShortUrl(this.data).subscribe(res => {
        console.log(res);
        this.shortUrl = 'https://shrtm.me/' + res.slug;
        this.success = true;
        this.isInvalid = false;
        this.createLinkForm.reset(); },
      err => {
        console.log(err);
        this.shortUrl = '';
        this.success = false;
        this.isInvalid = true;
        this.error = err.error.error;
      });

  }

  changePasswordVisibility(): void{
    if (this.type === 'password'){
      this.type = 'text';
      this.passwordVisibility = faEye;
    }
    else {
      this.type = 'password';
      this.passwordVisibility = faEyeSlash;
    }
  }

  copyToClipboard(): void {
    this.clipboard.copy(this.shortUrl);

  }
}

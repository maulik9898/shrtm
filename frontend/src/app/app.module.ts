import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {ShorturlService} from './shorturl.service';
import { PageRedirectComponent } from './page-redirect/page-redirect.component';

const routes: Routes = [
  {path: ':slug', component: PageRedirectComponent}
];

@NgModule({
  declarations: [
    AppComponent,
    PageRedirectComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(routes),
  ],
  providers: [ShorturlService],
  bootstrap: [AppComponent]
})
export class AppModule {

}

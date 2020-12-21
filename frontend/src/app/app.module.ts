import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { AppComponent } from './app.component';
import {HttpClientModule} from '@angular/common/http';
import {ShorturlService} from './shorturl.service';
import { PageRedirectComponent } from './page-redirect/page-redirect.component';
import { NotFoundComponent } from './not-found/not-found.component';

const routes: Routes = [
   {path: 'not-found', component: NotFoundComponent},
  {path: ':slug', component: PageRedirectComponent}

];

@NgModule({
  declarations: [
    AppComponent,
    PageRedirectComponent,
    NotFoundComponent
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
